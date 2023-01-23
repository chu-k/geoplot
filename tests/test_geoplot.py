import numpy as np
import geoplot
from geoplot import __version__

def test_version():
    assert __version__ == "0.1.0"

def test_triangle():
    tri = geoplot.triangle.Triangle(np.array((0,0)), 1)
    print(tri.points)
    tri.rotate2d(np.radians(90))
    print(tri.points)