import matplotlib.pyplot as plt
import numpy as np


def draw_shape(num_sides):
    if num_sides < 3:
        raise ValueError("A shape must have at least 3 sides.")

    # Calculate the coordinates for the shape based on the number of sides
    angle_increment = 2 * np.pi / num_sides
    angles = np.arange(0, 2 * np.pi, angle_increment)
    x_coords = np.cos(angles)
    y_coords = np.sin(angles)

    # Close the shape by appending the starting point to the end
    x_coords = np.append(x_coords, x_coords[0])
    y_coords = np.append(y_coords, y_coords[0])

    # Plot the shape
    plt.figure(figsize=(5, 5))
    plt.plot(x_coords, y_coords, 'b-')
    plt.fill(x_coords, y_coords, 'b', alpha=0.5)
    plt.axis('equal')
    plt.grid(True)
    plt.title(f"Shape with {num_sides} sides")
    plt.show()


# Test the method with different numbers of sides
try:
    num_sides = 9
    draw_shape(num_sides)
except ValueError as e:
    print(str(e))
