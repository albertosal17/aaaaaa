import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

import grid, patterns


def occupancy_rate(seed, n_gens, title=''):
    """
    A function used to compute the number of live cell at each generation during the game of life
    """
    game = grid.GameOfLife(seed=seed, title=title, display=False) #generate the object to play with

    # Lists to store generation numbers and corresponding occupancy rates
    generation_numbers = []
    occupancy_rates = []

    # Calculate and store the occupancy rate at each generation
    for frame in range(n_gens): #each generation corresponds to a frame in the animation

        #computing occupancy 
        total_cells = seed.size  #PROVA size is the number of element an array contains

        alive_cells = np.sum(game.state[game.state==1]) #number of alive cells 

        occupancy_rate = (alive_cells / total_cells) * 100 #occupancy rate as a percentage
        
        # storing results
        occupancy_rates.append(occupancy_rate)
        generation_numbers.append(frame + 1)

        # Update the game for the next generation
        game.update(frame=frame, display=False)
        
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(generation_numbers, occupancy_rates, linestyle='-', color='b')
    ax.set_title('Occupancy Rate Over Time')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Occupancy Rate (%)')
    ax.grid(True)
    plt.show()



#function for computing the number of times a pattern shows up
    #DOVREMMO CONSIDERARE UN PADDING DI ZERI ATTTORNO AL PATTERN AFFINCHE NON CI SIANO ERRORI?
    #E SE UN PATTERN APPARE ROVESCIATO O RUOTATO?
def period_of_replication(specie, size, n_gens): # we cannot use directly the seed for convolution as it has padding  
    
    seed = patterns.create_pattern(size=size, species=specie) # we need the seed to play the game though
    game = grid.GameOfLife(seed=seed, display=False) # define the game
    current_state = np.copy(game.state)
    
    for frame in range(1, n_gens+1): # start from one bc there is no update
        game.update(frame=frame, display=False)
        conv = convolve2d(game.state, np.flip(specie), mode='same', boundary='wrap') # PERCHE' IL FLIP? PROVA convolution between the current state and the specie we want to find
        
        if np.any(conv == np.sum(specie)):  # SE c'è almeno una cella in cui la verifica del pattern è stata confermata(->true) any sarà true
            print(f"Pattern repeated after {frame} generations")
            rep = True
            break
        else:
            rep = False
    if not rep:
        print("Pattern did not repeat within the specified number of generations")