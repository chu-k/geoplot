from abc import ABC

import numpy as np
from numpy.typing import ArrayLike

class Shape2d(ABC):

    def __init__(self, center: ArrayLike):
        self.center = center

    def get_center(self) -> ArrayLike:
        return self.center

    def create_npoints(self, inscribe_r:float):
        """https://math.stackexchange.com/questions/4114500"""
        points = []
        theta_k = 0.0
        n = self.num_points
        for k in range(n):
            theta_k = 2.0 * k * np.pi /n
            pt = self.center + inscribe_r / (2.0 * np.sin(np.pi/n)) * np.array((np.cos(theta_k), np.sin(theta_k)))
            points.append(pt)
        return np.array(points)

    def rotate2d(self, angle:float):
        """Rotate about centroid by angle."""
        shifted = self.points - self.center
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        shifted = shifted @ rot.T + self.center
        self.points = shifted