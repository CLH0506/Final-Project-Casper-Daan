import numpy as np
import random
import matplotlib.pyplot as plt

def plot_triangular_lattice(rows, max_steps, show_saw=True):
    # Adjust spacing based on the side length of the triangles
    side_length=rows//10
    cols=rows
    dx = side_length
    dy = side_length * np.sqrt(3) / 2

    # Create dictionaries to store the coordinates and neighbors
    lattice_points = {}
    lattice_neighbors = {}

    # Generate points and neighbors
    for row in range(rows):
        for col in range(cols):
            x = col * dx + (row % 2) * dx / 2
            y = row * dy
            point = (x, y)

            # Store coordinates
            lattice_points[(row, col)] = point

            # Determine neighbors
            neighbors = []
            for d_row, d_col in [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]:
                neighbor_row, neighbor_col = row + d_row, col + d_col
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    neighbors.append((neighbor_row, neighbor_col))
            
            lattice_neighbors[(row, col)] = neighbors

    # Plot the points
    x_coords, y_coords = zip(*lattice_points.values())
    plt.scatter(x_coords, y_coords, s=500//rows^2)

    # Perform and plot the self-avoiding walk if required
    if show_saw:
        saw_path = self_avoiding_walk(lattice_points, lattice_neighbors, rows, cols, max_steps, side_length)
        saw_x_coords, saw_y_coords = zip(*[lattice_points[p] for p in saw_path])
        plt.plot(saw_x_coords, saw_y_coords, color='red')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    plt.suptitle("Self-Avoiding Walk on a triangular lattice")

def self_avoiding_walk(lattice_points, lattice_neighbors, rows, cols, max_steps, side_length):
    # Start from the center of the lattice
    middle_point = (rows // 2, cols // 2)
    path = [middle_point]

    # Perform the walk
    while len(path) < max_steps:
        current_point = path[-1]
        neighbors = lattice_neighbors[current_point]
        unvisited_neighbors = [n for n in neighbors if n not in path]

        if not unvisited_neighbors:
            # No unvisited neighbors, walk is over
            break

        # Randomly shuffle unvisited neighbors to randomize selection
        random.shuffle(unvisited_neighbors)

        # Check if next step is valid
        for next_point in unvisited_neighbors:
            # Calculate the vector from the current to the next point
            current_pos = lattice_points[current_point]
            next_pos = lattice_points[next_point]
            step_vector = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

            # Calculate the length of the vector
            step_length = np.sqrt(step_vector[0]**2 + step_vector[1]**2)

            # Check if the step length is approximately equal to the side length
            if abs(step_length - side_length) < 1e-10:
                path.append(next_point)
                break
            plt.title(f"Lenght of walk: {len(path)}")
    return path

# Example usage
plot_triangular_lattice(10, 40)  #Number of rows and columns, maximum number of steps.