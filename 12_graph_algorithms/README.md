# Algorithms

## 1. Breadth-First Search (BFS)

BFS is an algorithm for traversing or searching tree or graph data structures. It starts at a selected node (often called the "root") and explores all of its neighbours at the present depth and then moves on to nodes at the next depth level.

At the heart BFS uses a queue to keep track of next nodes to visit.

*Advantages:*

1. Finds the shortest number of steps.
2. Finds all possible paths.

*Disadvantages:*

1. Memory consumption: BFS can consume a lot of memory, especially for wide trees or graphs, as it needs to store all nodes at the current depth level.
2. Slower than DFS: In some cases, BFS can be slower than depth-first search (DFS) due to the overhead of maintaining the queue.

*Usage:*

1. Finding the shortest path in unweighted graphs.
2. Level-order traversal of trees.
3. Number of days to spread a virus in a grid.
4. Solving puzzles with a state space (e.g., mazes, chess).

## 2. Depth-First Search (DFS)

DFS is another algorithm for traversing or searching tree or graph data structures. It starts at a selected node and explores as far as possible along each branch before backtracking.

At the heart of DFS is a stack (either implicit via recursion or explicit) to keep track of the next nodes to visit.

*Advantages:*

1. Low memory usage: DFS can be more memory-efficient than BFS, as it doesn't need to store all nodes at the current depth level.
2. Can find solutions more quickly: In some cases, DFS can find a solution faster than BFS, especially if the solution is deep in the tree.

*Disadvantages:*

1. May not find the shortest path: DFS does not guarantee the shortest path in unweighted graphs.
2. Can get stuck in deep branches: DFS may explore deep branches that do not lead to a solution, potentially taking longer to find a valid path.

*Usage:*

1. Puzzles with a state space (e.g., mazes, chess).
2. Graph coloring problems.
3. Recursive backtracking problems (e.g., N-Queens, Sudoku).
