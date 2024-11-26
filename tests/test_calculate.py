# tests/test_calculate.py

import unittest
import numpy as np
from refractulator import Refractulator

class TestRefractulator(unittest.TestCase):
    def setUp(self):
        self.refr = Refractulator(radius=1.0)
        self.D = np.array([1.0, 0.0, 0.0])
        self.ray_origins = np.array([
            [2.0, 0.0, 0.0],  # Directly in front
            [0.0, 2.0, 0.0],  # Offset
            [0.0, 0.0, 2.0]   # Another offset
        ])

    def test_calculate_normal_vector(self):
        point = np.array([1.0, 0.0, 0.0])
        normal = self.refr.calculate_normal_vector(point)
        expected = np.array([1.0, 0.0, 0.0])
        np.testing.assert_array_almost_equal(normal, expected)

    def test_line_sphere_intersection_no_intersection(self):
        P0 = np.array([0.0, 0.0, 3.0])
        D = np.array([0.0, 0.0, 1.0])
        intersections = self.refr.line_sphere_intersection(P0, D, self.refr.center, self.refr.radius)
        # Filter for positive t values
        positive_ts = [t for t in intersections if t > 0]
        self.assertEqual(positive_ts, [], "Expected no intersections in the positive direction.")


    def test_calculate_refracted_ray_total_internal_reflection(self):
        I = np.array([0.0, -1.0, 0.0])
        N = np.array([0.0, 1.0, 0.0])
        T = self.refr.calculate_refracted_ray(I, N, 1.0, 1.0)  # n1 = n2
        self.assertIsNotNone(T)
        np.testing.assert_array_almost_equal(T, I)

    def test_calculate_ray_no_intersection(self):
        P0 = np.array([0.0, 0.0, 3.0])
        D = self.D
        ray = self.refr.calculate_ray(P0, D, self.refr.n_air, self.refr.refractive_indices['red'], self.refr.radius, 'red')
        self.assertIsNone(ray)

    def test_calculate_ray_with_intersection(self):
        P0 = np.array([2.0, 0.0, 0.0])  # Starting outside the sphere
        D = np.array([-1.0, 0.0, 0.0])  # Direction towards the sphere
        ray = self.refr.calculate_ray(P0, D, self.refr.n_air, self.refr.refractive_indices['red'], self.refr.radius, 'red')
        self.assertIsNotNone(ray, "Ray should intersect the sphere and not be None.")
        self.assertIn('color', ray, "Ray should contain 'color' key.")
        self.assertIn('path', ray, "Ray should contain 'path' key.")
        # Additional assertions can be added to verify the ray's path


if __name__ == '__main__':
    unittest.main()
