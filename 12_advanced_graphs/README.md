# Advanced Graph Algorithms 🌐

> **Interview Frequency**: 45% | **Difficulty**: ⭐⭐⭐⭐ | **Pattern Priority**: #12

## 🎯 **Core Concept**
Advanced graph algorithms go beyond basic BFS/DFS to solve complex problems involving shortest paths, minimum spanning trees, network flows, and specialized graph structures.

## 🏢 **Company Focus**
- **Google**: Maps, search ranking, social networks
- **Meta**: Social graph, friend recommendations, news feed
- **Amazon**: Logistics, delivery optimization, warehouse routing
- **Apple**: Location services, device networks
- **Netflix**: Content recommendation graphs
- **Microsoft**: Network routing, cloud infrastructure

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra's Algorithm | Google, Amazon |
| [Cheapest Flights K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Modified Dijkstra | All FAANG |
| [Minimum Spanning Tree](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal's/Prim's | Google, Meta |
| [Find Critical Connections](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Tarjan's Algorithm | Google, Amazon |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union-Find | Meta, Google |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Algorithm | Time | Space |
|---------|------------|---------------|------|-------|
| [Dijkstra Shortest Path](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra | O(V²) / O(E log V) | O(V) |
| [Bellman-Ford](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford | O(VE) | O(V) |
| [Floyd-Warshall](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | All-Pairs Shortest | O(V³) | O(V²) |
| [Kruskal's MST](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Union-Find + Sort | O(E log E) | O(V) |
| [Topological Sort](https://leetcode.com/problems/course-schedule-ii/) | Medium | Kahn's Algorithm | O(V + E) | O(V) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | Topological Sort + Graph Building |
| [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Binary Search + Graph |
| [Bus Routes](https://leetcode.com/problems/bus-routes/) | Hard | BFS on Hypergraph |

## 🛠️ **Core Algorithms & Templates**

### **Algorithm 1: Dijkstra's Shortest Path**
```python
import heapq
from collections import defaultdict

def dijkstra_shortest_path(graph, start):
    """Find shortest paths from start to all vertices"""
    # Distance from start to each vertex
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, vertex = heapq.heappop(pq)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        # Update distances to neighbors
        for neighbor, weight in graph[vertex]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return distances

def network_delay_time(times, n, k):
    """LC 743: Network Delay Time"""
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Run Dijkstra from source k
    distances = dijkstra_shortest_path(graph, k)
    
    # Check if all nodes reachable
    max_time = 0
    for node in range(1, n + 1):
        if distances[node] == float('inf'):
            return -1
        max_time = max(max_time, distances[node])
    
    return max_time

class DijkstraOptimized:
    """Optimized Dijkstra with path reconstruction"""
    
    def shortest_path_with_path(self, graph, start, end):
        distances = {start: 0}
        previous = {}
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, vertex = heapq.heappop(pq)
            
            if vertex == end:
                break
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            for neighbor, weight in graph.get(vertex, []):
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = vertex
                        heapq.heappush(pq, (new_dist, neighbor))
        
        # Reconstruct path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous.get(current)
        
        return distances.get(end, float('inf')), path[::-1]
```

### **Algorithm 2: Bellman-Ford (Handles Negative Weights)**
```python
def bellman_ford(graph, start, num_vertices):
    """Find shortest paths, can handle negative weights"""
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:  # graph is list of edges
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    return distances

def cheapest_flights_k_stops(n, flights, src, dst, k):
    """LC 787: Cheapest Flights Within K Stops"""
    # Modified Bellman-Ford with at most k stops
    prices = [float('inf')] * n
    prices[src] = 0
    
    # At most k+1 iterations (k stops means k+1 flights)
    for _ in range(k + 1):
        temp_prices = prices[:]
        for u, v, price in flights:
            if prices[u] != float('inf'):
                temp_prices[v] = min(temp_prices[v], prices[u] + price)
        prices = temp_prices
    
    return prices[dst] if prices[dst] != float('inf') else -1

def bellman_ford_with_path_compression(edges, n, start):
    """Optimized Bellman-Ford with early termination"""
    dist = [float('inf')] * n
    dist[start] = 0
    
    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        
        if not updated:  # Early termination
            break
    
    # Check negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    
    return dist
```

### **Algorithm 3: Floyd-Warshall (All-Pairs Shortest Paths)**
```python
def floyd_warshall(graph):
    """Find shortest paths between all pairs of vertices"""
    n = len(graph)
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from vertex to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Fill in direct edges
    for u in range(n):
        for v, weight in graph[u]:
            dist[u][v] = weight
    
    # Floyd-Warshall algorithm
    for k in range(n):  # Intermediate vertex
        for i in range(n):  # Source
            for j in range(n):  # Destination
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_city_with_smallest_neighbors(n, edges, distance_threshold):
    """LC 1334: Find the City With Smallest Number of Neighbors"""
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Find city with smallest number of reachable neighbors
    min_neighbors = float('inf')
    result_city = 0
    
    for i in range(n):
        neighbors = sum(1 for j in range(n) 
                       if i != j and dist[i][j] <= distance_threshold)
        if neighbors <= min_neighbors:
            min_neighbors = neighbors
            result_city = i
    
    return result_city
```

### **Algorithm 4: Union-Find (Disjoint Set Union)**
```python
class UnionFind:
    """Efficient Union-Find with path compression and union by rank"""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False  # Already in same component
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        """Check if x and y are in same component"""
        return self.find(x) == self.find(y)
    
    def get_components_count(self):
        """Get number of connected components"""
        return self.components

def accounts_merge(accounts):
    """LC 721: Accounts Merge using Union-Find"""
    email_to_index = {}
    email_to_name = {}
    index = 0
    
    # Map emails to indices
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_index:
                email_to_index[email] = index
                email_to_name[email] = name
                index += 1
    
    # Create Union-Find structure
    uf = UnionFind(index)
    
    # Union emails within same account
    for account in accounts:
        if len(account) > 1:
            first_email_index = email_to_index[account[1]]
            for email in account[2:]:
                uf.union(first_email_index, email_to_index[email])
    
    # Group emails by root parent
    groups = defaultdict(list)
    for email, idx in email_to_index.items():
        root = uf.find(idx)
        groups[root].append(email)
    
    # Build result
    result = []
    for group in groups.values():
        group.sort()
        name = email_to_name[group[0]]
        result.append([name] + group)
    
    return result
```

### **Algorithm 5: Minimum Spanning Tree**
```python
def kruskal_mst(n, edges):
    """Kruskal's algorithm for MST using Union-Find"""
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_edges = []
    total_cost = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):  # If u and v not in same component
            mst_edges.append((u, v, weight))
            total_cost += weight
            
            if len(mst_edges) == n - 1:  # MST complete
                break
    
    return mst_edges, total_cost

def prim_mst(graph, start=0):
    """Prim's algorithm for MST using priority queue"""
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start, -1)]  # (weight, vertex, parent)
    mst_edges = []
    total_cost = 0
    
    while min_heap and len(mst_edges) < n - 1:
        weight, vertex, parent = heapq.heappop(min_heap)
        
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        if parent != -1:
            mst_edges.append((parent, vertex, weight))
            total_cost += weight
        
        # Add edges to unvisited neighbors
        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, vertex))
    
    return mst_edges, total_cost

def min_cost_connect_all_points(points):
    """LC 1584: Min Cost to Connect All Points"""
    n = len(points)
    
    # Generate all edges with Manhattan distance
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((i, j, dist))
    
    # Use Kruskal's algorithm
    return kruskal_mst(n, edges)[1]
```

### **Algorithm 6: Topological Sort**
```python
def topological_sort_kahn(graph, n):
    """Kahn's algorithm for topological sorting"""
    # Calculate in-degrees
    in_degree = [0] * n
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # Initialize queue with vertices having 0 in-degree
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex)
        
        # Reduce in-degree of neighbors
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    if len(topo_order) != n:
        return []  # Cycle detected
    
    return topo_order

def topological_sort_dfs(graph, n):
    """DFS-based topological sorting"""
    visited = [0] * n  # 0: unvisited, 1: visiting, 2: visited
    stack = []
    
    def dfs(vertex):
        if visited[vertex] == 1:  # Back edge - cycle detected
            return False
        if visited[vertex] == 2:  # Already processed
            return True
        
        visited[vertex] = 1  # Mark as visiting
        
        for neighbor in graph.get(vertex, []):
            if not dfs(neighbor):
                return False
        
        visited[vertex] = 2  # Mark as visited
        stack.append(vertex)
        return True
    
    for i in range(n):
        if visited[i] == 0:
            if not dfs(i):
                return []  # Cycle detected
    
    return stack[::-1]  # Reverse to get topological order

def course_schedule_ii(num_courses, prerequisites):
    """LC 210: Course Schedule II"""
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    return topological_sort_kahn(graph, num_courses)
```

### **Algorithm 7: Tarjan's Algorithm (Strongly Connected Components)**
```python
def tarjan_scc(graph):
    """Tarjan's algorithm for finding strongly connected components"""
    n = len(graph)
    ids = [-1] * n  # Node ids
    low = [0] * n   # Low values
    on_stack = [False] * n
    stack = []
    scc_components = []
    id_counter = 0
    
    def dfs(at):
        nonlocal id_counter
        stack.append(at)
        on_stack[at] = True
        ids[at] = low[at] = id_counter
        id_counter += 1
        
        # Visit neighbors
        for to in graph[at]:
            if ids[to] == -1:  # Unvisited
                dfs(to)
            if on_stack[to]:  # Part of current SCC
                low[at] = min(low[at], low[to])
        
        # Found SCC root
        if ids[at] == low[at]:
            component = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                component.append(node)
                if node == at:
                    break
            scc_components.append(component)
    
    for i in range(n):
        if ids[i] == -1:
            dfs(i)
    
    return scc_components

def critical_connections(n, connections):
    """LC 1192: Critical Connections in a Network (Bridges)"""
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    disc = [0] * n  # Discovery times
    low = [0] * n   # Low values
    parent = [-1] * n
    bridges = []
    time = [0]  # Use list for mutable reference
    
    def bridge_dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                bridge_dfs(v)
                
                # Update low value
                low[u] = min(low[u], low[v])
                
                # Check if edge (u, v) is a bridge
                if low[v] > disc[u]:
                    bridges.append([u, v])
            
            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            bridge_dfs(i)
    
    return bridges
```

## 📊 **Algorithm Complexity Analysis**

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| **Dijkstra** | O(V² / E log V) | O(V) | Single-source shortest path |
| **Bellman-Ford** | O(VE) | O(V) | Negative weights, cycle detection |
| **Floyd-Warshall** | O(V³) | O(V²) | All-pairs shortest paths |
| **Kruskal's MST** | O(E log E) | O(V) | Minimum spanning tree |
| **Prim's MST** | O(E log V) | O(V) | Minimum spanning tree |
| **Topological Sort** | O(V + E) | O(V) | DAG ordering |
| **Tarjan's SCC** | O(V + E) | O(V) | Strongly connected components |

## 🧠 **Advanced Patterns**

### **Pattern 1: Shortest Path Variants**
```python
def shortest_path_with_constraints(graph, start, end, max_stops):
    """Shortest path with maximum stops constraint"""
    # Use BFS with level tracking
    queue = deque([(start, 0, 0)])  # (node, cost, stops)
    min_cost = float('inf')
    
    while queue:
        node, cost, stops = queue.popleft()
        
        if node == end:
            min_cost = min(min_cost, cost)
            continue
        
        if stops < max_stops:
            for neighbor, weight in graph.get(node, []):
                if cost + weight < min_cost:  # Pruning
                    queue.append((neighbor, cost + weight, stops + 1))
    
    return min_cost if min_cost != float('inf') else -1

def shortest_path_visiting_all(graph, must_visit):
    """Shortest path visiting all required nodes (TSP variant)"""
    n = len(must_visit)
    dp = {}
    
    def tsp(mask, pos):
        if mask == (1 << n) - 1:  # Visited all nodes
            return 0
        
        if (mask, pos) in dp:
            return dp[(mask, pos)]
        
        result = float('inf')
        for next_pos in range(n):
            if not (mask & (1 << next_pos)):  # Not visited
                new_mask = mask | (1 << next_pos)
                cost = graph[must_visit[pos]][must_visit[next_pos]]
                result = min(result, cost + tsp(new_mask, next_pos))
        
        dp[(mask, pos)] = result
        return result
    
    # Try starting from each node
    min_cost = float('inf')
    for start in range(n):
        cost = tsp(1 << start, start)
        min_cost = min(min_cost, cost)
    
    return min_cost
```

### **Pattern 2: Graph Modification Problems**
```python
def min_edges_to_make_connected(n, connections):
    """LC 1319: Number of Operations to Make Network Connected"""
    if len(connections) < n - 1:
        return -1  # Not enough edges
    
    uf = UnionFind(n)
    redundant_edges = 0
    
    for u, v in connections:
        if not uf.union(u, v):
            redundant_edges += 1
    
    components = uf.get_components_count()
    return components - 1  # Need (components - 1) additional edges

def swim_in_rising_water(grid):
    """LC 778: Swim in Rising Water"""
    n = len(grid)
    
    def can_reach(max_height):
        if grid[0][0] > max_height:
            return False
        
        visited = [[False] * n for _ in range(n)]
        stack = [(0, 0)]
        visited[0][0] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while stack:
            row, col = stack.pop()
            
            if row == n - 1 and col == n - 1:
                return True
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < n and 0 <= nc < n and 
                    not visited[nr][nc] and grid[nr][nc] <= max_height):
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        
        return False
    
    # Binary search on the answer
    left, right = max(grid[0][0], grid[n-1][n-1]), max(max(row) for row in grid)
    
    while left < right:
        mid = (left + right) // 2
        if can_reach(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify the problem type**: "This looks like a shortest path problem"
2. **Choose appropriate algorithm**: "Since we have non-negative weights, Dijkstra is optimal"
3. **Discuss time/space tradeoffs**: "Floyd-Warshall gives us all-pairs but uses O(V²) space"

### **⚡ Algorithm Selection Guide**
- **Single-source shortest path**: Dijkstra (non-negative), Bellman-Ford (negative weights)
- **All-pairs shortest path**: Floyd-Warshall
- **Minimum spanning tree**: Kruskal (sparse), Prim (dense)
- **Cycle detection**: Union-Find, DFS
- **Topological ordering**: Kahn's algorithm, DFS

### **🐛 Common Pitfalls**
- **Negative weight cycles**: Use Bellman-Ford, not Dijkstra
- **Graph representation**: Choose adjacency list vs matrix wisely
- **Union-Find optimization**: Always use path compression and union by rank
- **MST uniqueness**: Multiple MSTs can exist with same total weight

## 🔍 **Problem Identification**

**Use Advanced Graph Algorithms when you see:**
- "Shortest path between..."
- "Minimum cost to connect..."
- "Network connectivity"
- "Critical connections/bridges"
- "Strongly connected components"
- "Course dependencies" (topological sort)
- "Union of accounts/groups"

## 📈 **Practice Schedule**

### **Week 1: Shortest Paths**
- Day 1-2: Dijkstra implementation and problems
- Day 3-4: Bellman-Ford and negative weight handling
- Day 5-7: Floyd-Warshall and all-pairs problems

### **Week 2: Union-Find & MST**
- Day 1-3: Union-Find data structure and applications
- Day 4-5: Kruskal's and Prim's algorithms
- Day 6-7: MST problems and variations

### **Week 3: Advanced Topics**
- Day 1-2: Topological sort problems
- Day 3-4: Tarjan's algorithm and SCCs
- Day 5-7: Complex graph problems and optimizations

## 🎖️ **Success Metrics**
- ✅ Implement Dijkstra, Bellman-Ford, Floyd-Warshall
- ✅ Master Union-Find with optimizations
- ✅ Solve MST problems efficiently
- ✅ Handle topological sorting confidently
- ✅ Understand when to use each algorithm

---

**Previous**: [← Graphs](../11_graphs/) | **Next**: [Back Tracking →](../13_back_tracking/)
