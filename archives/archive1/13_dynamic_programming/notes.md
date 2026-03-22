# Dynamic Programming

To avoid redundannt calculations, store results of subproblems to reuse later.
Approaches:
- Top-down (memoization): Recursion with caching of results.
- Bottom-up (tabulation): Iterative filling of a table based on smaller subproblems. (for loops)

| Top-down | Bottom-up |
|----------|-----------|
| Start with required case and go to base case and come back up | Start with base case and build up to required case |
| Easier to implement | Often more space efficient |
| Recursion with caching | Iterative with table filling |