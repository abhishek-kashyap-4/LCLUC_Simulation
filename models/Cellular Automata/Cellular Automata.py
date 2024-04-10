# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:37:47 2024

@author: kashy
"""

import numpy as np
import matplotlib.pyplot as plt

class LCLUC_CA:
    def __init__(self, size, initial_density=0.5, rule=30):
        self.size = size
        self.rule = rule
        self.grid = np.random.choice([0, 1], size=(size,), p=[1-initial_density, initial_density])

    def apply_rule(self, neighborhood):
        return (self.rule >> neighborhood) & 1

    def evolve(self, steps=1):
        for _ in range(steps):
            new_grid = np.zeros_like(self.grid)
            for i in range(self.size):
                left = self.grid[(i-1) % self.size]
                center = self.grid[i]
                right = self.grid[(i+1) % self.size]
                neighborhood = (left << 2) + (center << 1) + right
                new_grid[i] = self.apply_rule(neighborhood)
            self.grid = new_grid

    def plot(self):
        plt.imshow(self.grid.reshape(1, -1), cmap='Greys', interpolation='nearest')
        plt.show()

# Example usage
if __name__ == "__main__":
    ca = LCLUC_CA(100, initial_density=0.5, rule=30)
    ca.plot()
    ca.evolve(steps=50)
    ca.plot()
