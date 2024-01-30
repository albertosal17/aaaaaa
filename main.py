from tkinter import N
import numpy as np

import patterns, grid , terminal, analysis

#initializing things
#size = [38, 52] #size of the board, rows, col
size = [38, 150] #size of the board, rows, col
ON, OFF =  1, 0 # pixels values
seed = np.zeros(shape=size)

#initialization of the game 
seed = patterns.create_pattern(size=size, species=patterns.glider, noise=True)
game = grid.GameOfLife(seed=seed) 


#displaying evolution on terminal
import time
num_generations=15
current_grid=seed.copy()
for gen in range(1,num_generations):
    terminal.display_grid(current_grid)
    current_grid = game.update(gen)
    #time.sleep(0.1)  # Adjust the sleep time to control the speed of the animation
    input('')

analysis.period_of_replication(specie=patterns.glider, size=size, n_gens=num_generations)

