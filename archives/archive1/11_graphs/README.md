# Graphs 🕸️

> **Interview Frequency**: 70% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #11

## 🎯 **Core Concept**
Graphs represent relationships between entities using vertices and edges. Master BFS, DFS, and connected components for interview success.

## 🏢 **Company Focus**
- **Google**: Social networks, web graphs, complex graph algorithms
- **Meta**: Friend connections, social graph traversal
- **Amazon**: Delivery routes, recommendation systems
- **Apple**: Device networks, user interaction graphs  
- **Microsoft**: Network topology, dependency graphs

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | DFS/BFS on Grid | All FAANG |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Graph Traversal | Google, Meta |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Cycle Detection | All FAANG |
| [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Multi-source BFS | Google, Amazon |
| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | Tree Properties | Meta, Apple |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | BFS Shortest Path | O(M²×N) | O(M²×N) |
| [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | Boundary DFS | O(M×N) | O(M×N) |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Topological Sort | O(V+E) | O(V+E) |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union-Find/DFS | O(N log N) | O(N) |
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS | O(M×N) | O(M×N) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | Topological Sort + Trie |
| [Critical Connections](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Tarjan's Algorithm |
| [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | BFS with Obstacles |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Graph Representation**
```python
# Adjacency List (Most Common)
def build_adjacency_list(edges, n, directed=False):
    graph = {i: [] for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    
    return graph

# Example for different input formats
def build_graph_from_prerequisites(prerequisites, num_courses):
    """For course schedule problems"""
    graph = {i: [] for i in range(num_courses)}
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    return graph
```

### **Pattern 2: Depth-First Search (DFS)**
```python
def dfs_recursive(graph, start, visited=None):
    """Recursive DFS traversal"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph, start):
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors to stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

# Grid DFS Template
def dfs_grid(grid, row, col, visited):
    """DFS on 2D grid"""
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or 
        (row, col) in visited or 
        grid[row][col] == '0'):  # or whatever invalid condition
        return
    
    visited.add((row, col))
    
    # Visit all 4 directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        dfs_grid(grid, row + dr, col + dc, visited)
```

### **Pattern 3: Breadth-First Search (BFS)**
```python
from collections import deque

def bfs(graph, start):
    """BFS traversal"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def bfs_shortest_path(graph, start, end):
    """BFS to find shortest path"""
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found

# Grid BFS Template  
def bfs_grid(grid, start_row, start_col):
    """BFS on 2D grid"""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited.add((start_row, start_col))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Process current cell
        if grid[row][col] == 'target':
            return dist
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited and
                grid[new_row][new_col] != 'wall'):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1  # Target not reachable
```

### **Pattern 4: Connected Components**
```python
def count_connected_components(n, edges):
    """Count connected components using DFS"""
    graph = build_adjacency_list(edges, n)
    visited = set()
    components = 0
    
    for i in range(n):
        if i not in visited:
            dfs_component(graph, i, visited)
            components += 1
    
    return components

def dfs_component(graph, node, visited):
    """DFS to mark all nodes in current component"""
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_component(graph, neighbor, visited)

def number_of_islands(grid):
    """Classic connected components problem"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(row, col):
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            (row, col) in visited or 
            grid[row][col] == '0'):
            return
        
        visited.add((row, col))
        
        # Explore all 4 directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                dfs(row, col)
                islands += 1
    
    return islands
```

### **Pattern 5: Cycle Detection**
```python
def has_cycle_undirected(graph, n):
    """Cycle detection in undirected graph"""
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Back edge found
        
        return False
    
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    
    return False

def has_cycle_directed(graph, n):
    """Cycle detection in directed graph using DFS"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Back edge - cycle found
        if color[node] == BLACK:
            return False  # Already processed
        
        color[node] = GRAY
        
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        color[node] = BLACK
        return False
    
    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False
```

### **Pattern 6: Topological Sort**
```python
def topological_sort_kahn(graph, n):
    """Kahn's algorithm using BFS"""
    # Calculate in-degrees
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Start with nodes having no dependencies
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Remove this node and update in-degrees
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []  # Empty if cycle exists

def topological_sort_dfs(graph, n):
    """Topological sort using DFS"""
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
    
    return stack[::-1]  # Reverse to get topological order
```

## 📊 **Graph Algorithm Comparison**

| Algorithm | Use Case | Time Complexity | Space Complexity |
|-----------|----------|----------------|------------------|
| **DFS** | Path finding, connectivity | O(V + E) | O(V) |
| **BFS** | Shortest path (unweighted) | O(V + E) | O(V) |
| **Topological Sort** | Dependency ordering | O(V + E) | O(V) |
| **Connected Components** | Graph analysis | O(V + E) | O(V) |
| **Cycle Detection** | Validation | O(V + E) | O(V) |

## 🧠 **Key Insights**

### **DFS vs BFS Usage**
- **DFS**: Path existence, connected components, cycle detection
- **BFS**: Shortest path in unweighted graphs, level-by-level processing

### **Graph Representation Choice**
- **Adjacency List**: Best for sparse graphs, O(V + E) space
- **Adjacency Matrix**: Better for dense graphs, O(V²) space
- **Edge List**: Simple representation, O(E) space

### **Grid as Graph**
- **Cells as vertices**: Each cell is a node
- **Adjacent cells as edges**: 4-directional or 8-directional
- **Apply standard graph algorithms**: BFS/DFS work directly

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify graph type**: "Is this directed or undirected?"
2. **Discuss representation**: "I'll use adjacency list for efficiency"
3. **Explain algorithm choice**: "BFS gives shortest path in unweighted graphs"

### **⚡ Optimization Techniques**
- **Early termination**: Stop when target found
- **Bidirectional search**: Search from both ends
- **Visited set**: Avoid revisiting nodes

### **🐛 Common Pitfalls**
- **Not handling disconnected graphs**: Check all components
- **Infinite loops**: Ensure proper visited tracking
- **Wrong graph representation**: Directed vs undirected
- **Boundary conditions**: Grid problems need bounds checking

## 🔍 **Problem Identification**

**Use Graph algorithms when you see:**
- "Connected components"
- "Shortest path"
- "Dependencies" or "prerequisites"
- "Islands" or "regions"
- "Network" or "relationships"
- 2D grid traversal problems

## 📈 **Complexity Patterns**

| Graph Type | Vertices (V) | Edges (E) | Typical Complexity |
|------------|--------------|-----------|-------------------|
| **Sparse** | n | O(n) | O(V + E) = O(n) |
| **Dense** | n | O(n²) | O(V + E) = O(n²) |
| **Grid** | m×n | ~4×m×n | O(m×n) |
| **Tree** | n | n-1 | O(n) |

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Number of Islands, Clone Graph
- Day 3-4: DFS and BFS implementations
- Day 5-7: Connected Components problems

### **Week 2: Intermediate**
- Day 1-3: Course Schedule, Topological Sort
- Day 4-5: Word Ladder, Rotting Oranges
- Day 6-7: Pacific Atlantic Water Flow

### **Week 3: Advanced**
- Surrounded Regions
- Accounts Merge
- Critical Connections
- Mock interview practice

## 📋 **Graphs Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand graph representations (adjacency list/matrix)
- [ ] Master DFS and BFS traversal algorithms
- [ ] Know cycle detection in directed/undirected graphs
- [ ] Understand topological sorting
- [ ] Master Union-Find data structure

### **Essential Problems** (Must Complete)
- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) - Basic DFS/BFS
- [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) - Graph traversal
- [ ] [Course Schedule](https://leetcode.com/problems/course-schedule/) - Cycle detection
- [ ] [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Topological sort
- [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) - Multi-source BFS
- [ ] [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) - Union-Find
- [ ] [Valid Tree](https://leetcode.com/problems/graph-valid-tree/) - Tree validation

### **Intermediate Problems** (Build Proficiency)
- [ ] [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) - Multi-source BFS
- [ ] [Word Ladder](https://leetcode.com/problems/word-ladder/) - BFS shortest path
- [ ] [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Boundary DFS
- [ ] [Accounts Merge](https://leetcode.com/problems/accounts-merge/) - Union-Find application
- [ ] [Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Cycle detection
- [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) - Dijkstra's algorithm
- [ ] [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) - Path finding

### **Advanced Problems** (Expert Level)
- [ ] [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) - All shortest paths
- [ ] [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) - Topological sort
- [ ] [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) - Tarjan's algorithm
- [ ] [Minimum Spanning Tree](https://leetcode.com/problems/min-cost-to-connect-all-points/) - Kruskal/Prim
- [ ] [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Modified Dijkstra

### **Pattern Recognition** 🧠
- [ ] Identify when problem requires graph modeling
- [ ] Recognize grid problems as graph problems
- [ ] Spot shortest path requirements
- [ ] Know when to use DFS vs BFS
- [ ] Understand cycle detection applications

### **Implementation Skills** 💻
- [ ] Implement DFS and BFS from scratch
- [ ] Handle both directed and undirected graphs
- [ ] Use appropriate graph representation
- [ ] Implement Union-Find with optimizations
- [ ] Handle disconnected components

### **Interview Performance** 🎯
- [ ] Solve Number of Islands in under 5 minutes
- [ ] Implement DFS/BFS without reference
- [ ] Choose optimal graph representation
- [ ] Handle cycle detection questions
- [ ] Explain graph algorithm complexities

### **Progress Tracking**
- [ ] **Problems Solved**: ___/18+ problems completed
- [ ] **Time Investment**: ___/25+ hours practiced
- [ ] **Mock Interviews**: ___/3 graph focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Implement DFS and BFS from scratch
- ✅ Convert between graph representations
- ✅ Detect cycles in both directed and undirected graphs
- ✅ Apply topological sort correctly
- ✅ Handle grid-based graph problems

---

**Previous**: [← Backtracking](../10_backtracking/) | **Next**: [Advanced Graphs →](../12_advanced_graphs/)
