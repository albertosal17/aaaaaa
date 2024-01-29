import numpy as np

import patterns, grid , terminal

#initializing things
size = [70, 70] #size of the board
ON, OFF =  1, 0 # pixels values
seed = np.zeros(shape=size)

#setting seed
seed = patterns.create_pattern(size,species=patterns.GUN)
game = grid.GameOfLife(seed=seed)

#displaying evolution on terminal
import time

num_generations=100
current_grid=seed.copy()


for gen in range(1,num_generations):
    terminal.display_grid(current_grid)
    current_grid = game.update(gen)
    time.sleep(0.5)  # Adjust the sleep time to control the speed of the animation


