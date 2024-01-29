import numpy as np
from scipy.signal import convolve2d

class GameOfLife:

    def __init__(self, seed, title='', display=True):
        '''
        set the initial seed of the game
        '''
        self.state = seed
        #if display:
         #   self.fig, self.ax = draw_grid(title)
          #  self.timer = self.ax.text(1, 1, '', color='white', fontsize=12) # number of generation on top of the axes

    def count_neighbors(self):
        '''
            Returns the count of alive neighbors for each cell of the grid as a 2d ndarray,
            using a convolution with periodic boundary conditions
        '''
        
        fmap = np.array(
            [[1, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]]
        )
        return convolve2d(self.state, fmap, mode='same', boundary='wrap') # convolution between the state and fmap

    def update(self, frame, display=True):
        '''
            Computes the state of the next generation using Conway's rules. 
            Returns the plot of the grid at the next generation with a generation counter on top
        '''
        if frame < 1:   # no movement for the first step
            None
        else: 
            neighbors = self.count_neighbors()
            new_state = self.state.copy()
            
            for i in range(self.state.shape[0]):
                for j in range(self.state.shape[1]):
                    is_alive = self.state[i,j]
                    total = neighbors[i,j]
                    if (total < 2) or (total > 3): new_state[i,j] = 0
                    if total == 2 and is_alive == 1: new_state[i,j] = 1
                    if total == 3: new_state[i,j] = 1
            self.state = new_state
         # set the number of generation 
        #if display:
         #   message = f"Gen.{frame}"
          #  self.timer.set_text(message)
           # return draw_plot(self.fig, self.ax, self.state), self.timer
        #else:
        return self.state