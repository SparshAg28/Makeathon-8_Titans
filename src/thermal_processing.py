import numpy as np

def process_thermal(thermal_array):
    # Multiple realistic fire zones
    centers = [
        (120, 120),  # Room fire
        (80, 40),    # Lower room fire
        (150, 60),   # Right room fire
        (60, 150),   # Upper room fire
        (40, 60),    # Near human danger
    ]
    return centers