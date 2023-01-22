import numpy as np
import geoplot
from geoplot import __version__

def test_version():
    assert __version__ == "0.1.0"

def test_triangle():
    tri = geoplot.triangle.Triangle(np.random.random(2), 5)
    print(tri.points)