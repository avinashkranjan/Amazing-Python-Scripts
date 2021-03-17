<h1 align="center">A Star Path Finding Algorithm (Python Implementaion)</h1>
A python visualization of the A* path finding algorithm. Allows the user to input the starting node, ending node and barrier nodes to visualize the whole process of finding the path.

---------------------------------------------------------------------
## How it works

- Pygame module draws out the grids and sets up the application window, such that the colour of each node can be varied.

- Methods are created to change the colour and functionalities of nodes,
    - For left click:- *The first click and seconod click being the start point and end point respectively*, followed by setting up barriers between the two nodes for every click.
    - For right click:- Deleting the setup barrier.

- A-star algorithm is implemented -
    - `heuristics` function returns approimate distance between *start* and *end* points.
    - `update_neighbours` method is used to find out the neighbour nodes of the current node.
    - `open_set` queue keeps a list of tuples containing neighbour nodes information as #(fscore, count, node)
    - `g_score` storing G score of all neighbour nodes of the current node
    - `f_score` storing G score of all neighbour nodes of the current node

- Algorithm is called upon pressing `ENTER`/`RETURN` key
- All inputs reset upon pressing `SPACE BAR` key

---------------------------------------------------------------------
## Requirements (Py modules used)
- pygame
- queue

[](images/1.png)