
from threading import stack_size
import numpy as np

def create_pattern(size, species, offset=[0, 0], world=None, noise=False):
    '''
        Add a given species to the initial seed of the game
    '''
    #initializing world/environment
    if world is None: world = np.zeros(size, dtype=int) #se non si è scelto di lavorare in un ambiente specifico->tutte celle morte

    #initializing the pattern
    pattern = np.zeros(size, dtype=int)


    start_row, start_col = offset[0] + size[0] // 2 - 1, offset[1] + size[1] // 2 - 1 #PROVA position of the central cell
    pattern[start_row:(start_row + species.shape[0]), start_col:(start_col + species.shape[1])] = species # 'import' the pattern 
    
    if noise==True: 
        noise = np.zeros(size, dtype=int)
        p_alive = 0.4
        noise[start_row:(start_row + species.shape[0]), start_col:(start_col + species.shape[1])] = np.random.choice(a=[0,1], size=species.shape, p=[1-p_alive, p_alive])
        pattern = np.bitwise_or(pattern, noise)

    return np.bitwise_or(pattern, world) #element-wise sum


def create_random(size, p_alive=0.5, world=None):
    '''
        Add random noise to the initial seed of the game
    '''

    #initializing world/environment
    if world is None: world = np.zeros(size, dtype=int) 

    #initializing the pattern
    random_pattern = np.random.choice(a=[0,1], size=size, p=[1-p_alive, p_alive]) 

    return np.bitwise_or(random_pattern, world)


flower = np.array([[0, 1, 0], 
                   [1, 0, 1], 
                   [0, 1, 0]])

toad = np.array([[0, 1, 1, 1], 
                 [1, 1, 1, 0]])

glider = np.array([[1, 1, 1],
                   [0, 0, 1],
                   [0, 1, 0]])

gun = np.zeros((9,36), dtype=int) #RIVEDERNE LE PROPRIETA'
gun[4, 0] = gun[5,0] = 1 
gun[4, 1] = gun[5,1] = 1
gun[4, 10] = gun[5,10] = gun[6,10]= 1
gun[3, 11] = gun[7,11] =  1
gun[2, 12] = gun[8,12] =  1
gun[2, 13] = gun[8,13] =  1
gun[5, 14] =  1
gun[3, 15] = gun[7,15] =  1
gun[4, 16] = gun[5,16] = gun[6,16]= 1
gun[5,17] = 1
gun[2, 20] = gun[3,20] = gun[4,20]= 1
gun[2, 21] = gun[3,21] = gun[4,21]= 1
gun[1, 22] = gun[5,22] =  1
gun[0, 24] = gun[1,24] = gun[5,24]=gun[6,24]= 1
gun[2, -1] = gun[3,-1] = 1
gun[2, -2] = gun[3,-2] = 1

GUN = gun