print("Hello World!")
print("SAW for normal lattice")
import matplotlib.pyplot as plt
import numpy as np

# normal lattice
def saw(steps):
    x, y = [0], [0]
    visited = set([(0, 0)])

    for _ in range(steps):
        # Generate a random move (up, down, left, or right)
        move = np.random.choice(['up', 'down', 'left', 'right'])

        # Apply the move
        if move == 'up':
            next_point = (x[-1], y[-1] + 1)
        elif move == 'down':
            next_point = (x[-1], y[-1] - 1)
        elif move == 'left':
            next_point = (x[-1] - 1, y[-1])
        elif move == 'right':
            next_point = (x[-1] + 1, y[-1])

        # Check if the proposed move is valid (not visited)
        if next_point not in visited:
            x.append(next_point[0])
            y.append(next_point[1])
            visited.add(next_point)
            
            

    return x, y,

def plot_saw(x, y):
    plt.plot(x, y, marker='o')
    plt.title('Self-Avoiding Walk')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show(block=True)

# Number of steps for the self-avoiding walk
saw_steps = 100

# Generate self-avoiding walk coordinates
saw_x, saw_y = saw(saw_steps)

# Plot the self-avoiding walk
plot_saw(saw_x, saw_y)
