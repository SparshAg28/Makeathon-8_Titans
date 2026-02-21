import numpy as np

def create_occupancy_grid(df, map_size=20, resolution=0.1):
    grid_size = int(map_size / resolution)
    grid = np.zeros((grid_size, grid_size), dtype=int)

    for _, row in df.iterrows():
        if row["z"] > 0.1:
            x_idx = int(row["x"] / resolution)
            y_idx = int(row["y"] / resolution)

            if 0 <= x_idx < grid_size and 0 <= y_idx < grid_size:
                grid[x_idx][y_idx] = 1  # obstacle

    return grid