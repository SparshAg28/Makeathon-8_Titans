def apply_heat_to_grid(grid, heat_centers, resolution=0.1):
    for (x, y) in heat_centers:
        gx = int(x / resolution)
        gy = int(y / resolution)

        if 0 <= gx < grid.shape[0] and 0 <= gy < grid.shape[1]:
            grid[gx][gy] = 2  # 2 = heat danger
   
    return grid