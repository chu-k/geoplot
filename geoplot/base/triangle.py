from .shape import Shape2d

from numpy.typing import ArrayLike
import numpy as np

class Triangle(Shape2d):

    def __init__(self, center: ArrayLike, len: float):
        Shape2d.__init__(self, center)
        self.num_points = 3
        self.size = len
        self.points = self.create_npoints(len)
