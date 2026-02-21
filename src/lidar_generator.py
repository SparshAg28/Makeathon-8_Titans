import numpy as np
import pandas as pd

def generate_lidar(map_size=20, height=3, resolution=0.2):
    points = []

    # Outer walls
    for z in np.arange(0, height, resolution):
        for y in np.arange(0, map_size, resolution):
            points.append([0, y, z, 0.9])
            points.append([map_size, y, z, 0.9])
        for x in np.arange(0, map_size, resolution):
            points.append([x, 0, z, 0.9])
            points.append([x, map_size, z, 0.9])

    # Internal Room Walls
    for z in np.arange(0, height, resolution):
        for y in np.arange(0, map_size/2, resolution):
            points.append([map_size/2, y, z, 0.9])

        for x in np.arange(map_size/2, map_size, resolution):
            points.append([x, map_size/2, z, 0.9])

    # Clear Human (Cylinder Body + Head)
    center = (5, 5)

    # Body
    for z in np.arange(0, 1.5, 0.1):
        for angle in np.arange(0, 2*np.pi, 0.15):
            x = center[0] + 0.35*np.cos(angle)
            y = center[1] + 0.35*np.sin(angle)
            points.append([x, y, z, 0.6])

    # Head
    for z in np.arange(1.5, 1.8, 0.1):
        for angle in np.arange(0, 2*np.pi, 0.15):
            x = center[0] + 0.2*np.cos(angle)
            y = center[1] + 0.2*np.sin(angle)
            points.append([x, y, z, 0.6])

    df = pd.DataFrame(points, columns=["x","y","z","intensity"])
    return df