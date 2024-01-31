import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class SquareLattice:
    def __init__(self, size):
        self.size = size
        self.grid = [[False for _ in range(size)] for _ in range(size)]
        self.walk = []
        if starting_pos== 1: self.start_position=(size//2, size//2)
        elif starting_pos== 0:self.start_position=(0, 0)
        else: raise ValueError("starting_pos value must be 0 or 1")
        self.grid[self.start_position[0]][self.start_position[1]] = True
        self.walk.append(self.start_position)

    def is_valid_step(self, position):
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size and not self.grid[x][y]

    def add_step(self, position):
        if self.is_valid_step(position):
            self.grid[position[0]][position[1]] = True
            self.walk.append(position)
            return True
        return False

    def get_neighbors(self, position):
        x, y = position
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        random.shuffle(neighbors)  # Randomize to add variation
        return neighbors

    def grow_saw(self, length):
        while len(self.walk) < length:
            current_position = self.walk[-1]
            neighbors = self.get_neighbors(current_position)
            if not any(self.add_step(neighbor) for neighbor in neighbors):
                break  # No valid move, stop the walk
        print(len(self.walk))

    def visualize_walk(self):
        x_coords, y_coords = zip(*self.walk)
        plt.figure(figsize=(5, 5))
        plt.plot(x_coords, y_coords, marker='o', markersize=3.5, color='red')

        # Set limits and ticks for axes
        plt.xlim(-0.5 , self.size -0.5)
        plt.ylim(-0.5 , self.size -0.5)
        ax = plt.gca()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(scalar))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(scalar))

        plt.suptitle('Self-Avoiding Walk on a Square Lattice')
        plt.title(f"Lenght of walk: {len(self.walk)}")
        plt.grid(True)
        plt.show()



# Usage

starting_pos = 1                # 0 = (0,0), 1= middle of the grid (size//2, size//2)
size= 11                        # Size of the lattice
length = 100                    # Desired length of the SAW
scalar= int(size/10)
lattice = SquareLattice(size)
lattice.grow_saw(length)
lattice.visualize_walk()

