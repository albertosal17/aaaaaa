import numpy as np
import matplotlib.pyplot as plt
import grid

def occupancy_rate(seed, n_gens, title=''):
    
    game = grid.GameOfLife(seed, title, display=False)

    # Lists to store generation numbers and corresponding occupancy rates
    generation_numbers = []
    occupancy_rates = []

    for frame in range(n_gens):
        # Calculate and store the occupancy rate at each generation
        total_cells = seed.size  #the dimension of the size that we chose  
        alive_cells = np.sum(game.state[game.state==1]) #number of alive cells 
        occupancy_rate = (alive_cells / total_cells) * 100 #occupancy rate as a percentage
        occupancy_rates.append(occupancy_rate)
        generation_numbers.append(frame + 1)

        # Update the game for the next generation
        game.update(frame, display=False)
        
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(generation_numbers, occupancy_rates, linestyle='-', color='b')
    ax.set_title('Occupancy Rate Over Time')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Occupancy Rate (%)')
    ax.grid(True)
    plt.show()

def period_of_replication(seed, n_gens):
    
    game = grid.GameOfLife(seed, display=False)
    current_state = np.copy(game.state)
    
    for frame in range(1, n_gens+1):
        game.update(frame=frame, display=False)
        if np.all(game.state == seed):
            print(f"Pattern repeated after {frame} generations")
            rep = True
            break
        else:
            rep = False
    if not rep:
        print("Pattern did not repeat within the specified number of generations")