import numpy as np

from src.lidar_generator import generate_lidar
from src.occupancy_grid import create_occupancy_grid
from src.clustering import detect_clusters
from src.thermal_processing import process_thermal
from src.fusion import apply_heat_to_grid
from src.planner import astar
# Generate LiDAR
df = generate_lidar()

# Create occupancy grid
grid = create_occupancy_grid(df)

# Detect clusters
df = detect_clusters(df)

# Fake thermal sample
thermal = np.random.randint(20, 80, (200, 200))
heat_centers = process_thermal(thermal)

# Fusion
grid = apply_heat_to_grid(grid, heat_centers)

# Plan path
start = (10,10)
goal = (150,150)
path = astar(grid, start, goal)

print("Path length:", len(path))


import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(8,8))

# Show grid
# 0 = free (white)
# 1 = obstacle (black)
# 2 = heat (red)
display_grid = grid.copy()

# Create custom color map
from matplotlib.colors import ListedColormap
cmap = ListedColormap(["white", "black", "red"])

plt.imshow(display_grid.T, origin='lower', cmap=cmap)

# Draw path if exists
if path:
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    plt.plot(xs, ys, color='blue', linewidth=2)

# Mark start and goal
plt.scatter(start[0], start[1], color='green', s=100, label='Start')
plt.scatter(goal[0], goal[1], color='purple', s=100, label='Goal')

plt.legend()
plt.title("DRONY - Occupancy Grid with Path")
plt.show()