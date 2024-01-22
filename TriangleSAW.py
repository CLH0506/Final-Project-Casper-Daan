import matplotlib.pyplot as plt
import numpy as np

def plot_triangular_lattice(rows, cols, side_length):
    # Adjust spacing based on the side length of the triangles
    dx = side_length
    dy = side_length * np.sqrt(3)/2

    # Create lists to store the x and y coordinates
    x_coords = []
    y_coords = []

    # Generate points
    for row in range(rows):
        for col in range(cols):
            x = col * dx + (row % 2) * dx / 2
            y = row * dy
            x_coords.append(x)
            y_coords.append(y)

    # Plot the points
    plt.scatter(x_coords, y_coords)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
plot_triangular_lattice(10, 10, 1)
