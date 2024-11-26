# refractulator/calculate.py

import numpy as np

class Refractulator:
    def __init__(self, radius=1.0):
        self.center = np.array([0.0, 0.0, 0.0])
        self.n_air = 1.000293  # Air
        self.refractive_indices = {
            'red': 1.331,
            'orange': 1.332,
            'yellow': 1.333,
            'green': 1.335,
            'blue': 1.338,
            'violet': 1.342
        }
        self.radius = radius

    def calculate_normal_vector(self, point):
        """
        Calculate the normal vector at a specific point on the sphere surface.
        """
        normal_vector = point - self.center
        normal_vector /= np.linalg.norm(normal_vector)
        return normal_vector

    def line_sphere_intersection(self, P0: np.ndarray, D: np.ndarray, center: np.ndarray, radius: float) -> list[float]:
        """
        Find the intersection points of a line and a sphere.
        """
        a = np.dot(D, D)
        oc = P0 - center
        b = 2 * np.dot(D, oc)
        c = np.dot(oc, oc) - radius ** 2

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []  # No intersection
        sqrt_disc = np.sqrt(discriminant)
        t1 = (-b + sqrt_disc) / (2 * a)
        t2 = (-b - sqrt_disc) / (2 * a)
        return [t1, t2]

    def calculate_refracted_ray(self, I, N, n1, n2):
        """
        Calculate the refracted ray vector using Snell's Law.
        """
        cos_theta_i = -np.dot(N, I)
        sin2_theta_t = (n1 / n2) ** 2 * (1 - cos_theta_i ** 2)
        if sin2_theta_t > 1.0:
            return None  # Total internal reflection
        cos_theta_t = np.sqrt(1 - sin2_theta_t)
        T = (n1 / n2) * I + (n1 / n2 * cos_theta_i - cos_theta_t) * N
        T /= np.linalg.norm(T)
        return T

    def calculate_reflected_ray(self, I, N):
        """
        Calculate the reflected ray vector.
        """
        R = I - 2 * np.dot(I, N) * N
        R /= np.linalg.norm(R)
        return R

    def calculate_ray(self, P0, D, n1, n2, radius, color):
        """
        Calculate a single ray path interacting with the sphere.
        """
        # Entry point calculations
        t_values = self.line_sphere_intersection(P0, D, self.center, radius)
        t_values = sorted([t for t in t_values if t > 0])
        if len(t_values) == 0:
            return None  # Ray does not intersect the sphere
        t_entry = t_values[0]

        P_entry = P0 + D * t_entry
        N_entry = self.calculate_normal_vector(P_entry)
        I_entry = D

        # Refracted ray inside the sphere
        T_inside = self.calculate_refracted_ray(I_entry, N_entry, n1, n2)
        if T_inside is None:
            return None  # Total internal reflection

        # Internal reflection calculations
        t_values_inside = self.line_sphere_intersection(P_entry, T_inside, self.center, radius)
        t_values_inside = sorted([t for t in t_values_inside if t > 1e-6])
        if len(t_values_inside) == 0:
            return None  # Ray does not intersect internally
        t_reflect = t_values_inside[0]

        P_reflect = P_entry + T_inside * t_reflect
        N_reflect = self.calculate_normal_vector(P_reflect)
        I_reflect = T_inside

        # Reflected ray inside the sphere
        R_inside = self.calculate_reflected_ray(I_reflect, N_reflect)

        # Exit point calculations
        t_values_exit = self.line_sphere_intersection(P_reflect, R_inside, self.center, radius)
        t_values_exit = sorted([t for t in t_values_exit if t > 1e-6])
        if len(t_values_exit) == 0:
            return None  # Ray does not exit the sphere
        t_exit = t_values_exit[0]

        P_exit = P_reflect + R_inside * t_exit
        N_exit = -self.calculate_normal_vector(P_exit)
        I_exit = R_inside

        # Refracted ray exiting the sphere
        T_exit = self.calculate_refracted_ray(I_exit, N_exit, n2, n1)
        if T_exit is None:
            return None  # Total internal reflection at exit

        # Extend the exiting ray for visualization
        P_end = P_exit + T_exit * 10  # Adjust the factor as needed for visibility

        # Collect the ray path
        ray = {
            "color": color,
            "path": {
                "incoming": [P0.tolist(), P_entry.tolist()],
                "inside1": [P_entry.tolist(), P_reflect.tolist()],
                "inside2": [P_reflect.tolist(), P_exit.tolist()],
                "outgoing": [P_exit.tolist(), P_end.tolist()]
            }
        }
        return ray


    def get_perpendicular_vectors(self, D):
        """
        Return two vectors that are orthogonal to D and to each other.
        """
        D = np.asarray(D).flatten()
        if abs(D[0]) < 0.9:
            v = np.array([1, 0, 0])
        else:
            v = np.array([0, 1, 0])
        orthogonal_vector1 = np.cross(D, v)
        orthogonal_vector1 /= np.linalg.norm(orthogonal_vector1)
        orthogonal_vector2 = np.cross(D, orthogonal_vector1)
        orthogonal_vector2 /= np.linalg.norm(orthogonal_vector2)
        return orthogonal_vector1, orthogonal_vector2
    

    def calculate_rays_cylinder(self, ray_origins, D):
        """
        Calculate rays forming a cylindrical beam of parallel rays interacting with the sphere.
        """
        rays = []
        n1 = self.n_air  # Index of refraction outside the sphere

        for P0 in ray_origins:
            for color, n2 in self.refractive_indices.items():
                ray = self.calculate_ray(P0, D, n1, n2, self.radius, color)
                if ray:
                    rays.append(ray)
        return rays
    
