def apply_heat_to_grid(grid, heat_centers):
    fire_sizes = [10, 8, 12, 6, 7]  # Different radius per fire

    for idx, (x, y) in enumerate(heat_centers):
        radius = fire_sizes[idx % len(fire_sizes)]

        for i in range(-radius, radius):
            for j in range(-radius, radius):
                gx = x + i
                gy = y + j

                if 0 <= gx < grid.shape[0] and 0 <= gy < grid.shape[1]:
                    grid[gx][gy] = 2  # Heat zone

    return grid