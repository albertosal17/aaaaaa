# LCP-Project
Implementing Conway's Game of Life

## Assignment
* Start off implementing the GoF's rules and play with simple seeds in small dimensions;
* Increase the size of the GoF's world and play with more advanced patterns;
* Implement examples of the three categories of patterns still lifes, oscillators and spaceships;
* Analyse the evolutions of the patters in terms of frequency, replication, occupancy, etc.

  ## Basic rules
* Any live cell with fewer than two live neighbors dies, as if by underpopulation;
* Any live cell with two or three live neighbors lives on to the next generation;
* Any live cell with more than three live neighbors dies, as if by overpopulation;
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

A single cell has a total of 8 neighbouring cells i.e. left, right, top, bottom + diagonals.
