import matplotlib.pyplot as plt
import numpy as np
from base import triangle

if __name__ == "__main__":
    tri = triangle.Triangle(np.random.random(2), 5)
    print(tri.points)
    t1 = plt.Polygon(tri.points[:3,:], color='b')
    plt.gca().add_patch(t1)

    plt.savefig("test.png")