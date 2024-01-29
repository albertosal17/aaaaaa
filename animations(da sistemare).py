import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


import grid

#plot and grid have to be separate functions because of how matplotlib animations work (imshow is an artist)
def draw_plot(fig, ax, grid):
    '''
        function that draws the state of the world on a grid as a colormap
    '''
    state = np.flip(grid)
    #change the values of on and off here
    #state[state==0] = 
    #state[state==1] = 
    plt.set_cmap('gray')
    return ax.imshow(state)

def draw_grid(title=''):
    '''
        function that defines the visual properties of the grid
    '''
    fig, ax = plt.subplots()
    plt.axis('off')
    plt.grid(True)
    plt.title(title)
    return fig, ax


def play_gol(seed, n_gens, delta_t, title=''):
    '''
        Plays the game given the initial population(the seed) for a number of generations (n_gens)
        at period delta_t. Returns an animation FuncAnimation of plots for all the generations
    '''
    game = grid.GameOfLife(seed, title)
    anim = FuncAnimation(game.fig, game.update, frames=n_gens, interval=delta_t)
    HTML(anim.to_jshtml());
    return anim