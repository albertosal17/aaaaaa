import os

def display_grid(grid):
    #os.system('clear')  # For Unix/Linux
    os.system('cls')  # For Windows
    
    for row in grid:
        print("".join(['♥' if cell else '⋅' for cell in row]))
