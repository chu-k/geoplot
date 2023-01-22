from .shape import Shape2d

from numpy.typing import ArrayLike
import numpy as np

class Triangle(Shape2d):

    def __init__(self, center: ArrayLike, len: float):
        Shape2d.__init__(self, center)
        self.num_points = 3
        self.points = self._triangulate(center, len)

    def _triangulate(self, center: ArrayLike, len: float):
        """Return three points making an equilateral triangle.
        https://math.stackexchange.com/questions/4114500
        """
        points = []
        theta_k = 0.0
        n = self.num_points
        for k in range(self.num_points):
            theta_k += 2.0 * k * np.pi /n 
            pt = self.center + len / (2.0 * np.sin(np.pi/n)) * np.array((np.cos(theta_k), np.sin(theta_k)))
            points.append(pt)
        return np.array(points)
            