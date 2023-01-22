from abc import ABC
from typing import Union

from numpy.typing import ArrayLike

class Shape2d(ABC):

    def __init__(self, center: ArrayLike):
        self.center = center

    def get_center(self) -> ArrayLike:
        return self.center