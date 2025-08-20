# Greedy Algorithms 🎯

> **Interview Frequency**: 40% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #14

## 🎯 **Core Concept**
Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They work when the problem has optimal substructure and the greedy choice property.

## 🏢 **Company Focus**
- **Google**: Ad placement optimization, resource allocation
- **Meta**: News feed ranking, content scheduling
- **Amazon**: Delivery route optimization, warehouse management
- **Apple**: Battery life optimization, resource scheduling
- **Netflix**: Content delivery optimization
- **Microsoft**: Cloud resource allocation, meeting scheduling

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Best Time to Buy/Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | Peak Valley | All FAANG |
| [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Farthest Reach | Google, Meta |
| [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | Circular Array | Amazon, Apple |
| [Activity Selection](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Interval Scheduling | Google, Microsoft |
| [Minimum Platforms](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Event Scheduling | All FAANG |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Two Pointers Greedy | O(N) | O(1) |
| [Candy Distribution](https://leetcode.com/problems/candy/) | Hard | Two Pass Greedy | O(N) | O(N) |
| [Fractional Knapsack](https://www.geeksforgeeks.org/fractional-knapsack-problem/) | Medium | Value/Weight Ratio | O(N log N) | O(1) |
| [Minimum Spanning Tree](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal's/Prim's | O(E log E) | O(V) |
| [Huffman Coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/) | Medium | Priority Queue | O(N log N) | O(N) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Smallest String With Swaps](https://leetcode.com/problems/smallest-lexicographically-string-after-applying-operations/) | Medium | Greedy + Union-Find |
| [Minimum Number of Arrows](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Greedy Interval Processing |
| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Greedy Frequency Management |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Interval Scheduling Problems**
```python
def activity_selection(intervals):
    """Classic activity selection - maximum non-overlapping intervals"""
    if not intervals:
        return 0
    
    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])
    
    count = 1
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= last_end:  # Non-overlapping
            count += 1
            last_end = end
    
    return count

def non_overlapping_intervals(intervals):
    """LC 435: Minimum intervals to remove for non-overlapping"""
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    
    count = 0
    last_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:  # Overlapping
            count += 1  # Remove current interval
        else:
            last_end = intervals[i][1]  # Update end time
    
    return count

def meeting_rooms_ii(intervals):
    """LC 253: Minimum meeting rooms required"""
    if not intervals:
        return 0
    
    # Create events: start = +1 room, end = -1 room
    events = []
    for start, end in intervals:
        events.append((start, 1))    # Meeting starts
        events.append((end, -1))     # Meeting ends
    
    # Sort events by time, end events before start events at same time
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_rooms = 0
    current_rooms = 0
    
    for time, delta in events:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms

def minimum_arrows_burst_balloons(points):
    """LC 452: Minimum arrows to burst all balloons"""
    if not points:
        return 0
    
    # Sort by end coordinate
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    arrow_position = points[0][1]
    
    for start, end in points[1:]:
        if start > arrow_position:  # Need new arrow
            arrows += 1
            arrow_position = end
    
    return arrows
```

### **Pattern 2: Stock Trading Problems**
```python
def max_profit_unlimited_transactions(prices):
    """LC 122: Best Time to Buy and Sell Stock II"""
    if not prices:
        return 0
    
    total_profit = 0
    
    # Greedy: capture every profitable transaction
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    
    return total_profit

def max_profit_with_fee(prices, fee):
    """LC 714: Best Time to Buy and Sell Stock with Transaction Fee"""
    if not prices:
        return 0
    
    hold = -prices[0]  # Maximum profit when holding stock
    sold = 0           # Maximum profit when not holding stock
    
    for i in range(1, len(prices)):
        # Either keep holding or buy today
        hold = max(hold, sold - prices[i])
        # Either keep not holding or sell today (pay fee)
        sold = max(sold, hold + prices[i] - fee)
    
    return sold

def max_profit_k_transactions(prices, k):
    """LC 188: Best Time to Buy and Sell Stock IV (Greedy for large k)"""
    if not prices or k == 0:
        return 0
    
    # If k >= n/2, we can do as many transactions as we want
    if k >= len(prices) // 2:
        return max_profit_unlimited_transactions(prices)
    
    # DP approach for limited transactions
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices[1:]:
        for j in range(k, 0, -1):
            sell[j] = max(sell[j], buy[j] + price)
            buy[j] = max(buy[j], sell[j-1] - price)
    
    return sell[k]
```

### **Pattern 3: Array/String Greedy Problems**
```python
def jump_game(nums):
    """LC 55: Jump Game - can reach last index"""
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:  # Cannot reach this position
            return False
        
        farthest = max(farthest, i + nums[i])
        
        if farthest >= len(nums) - 1:  # Can reach end
            return True
    
    return False

def jump_game_ii(nums):
    """LC 45: Jump Game II - minimum jumps to reach end"""
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    # We don't need to jump from the last position
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        # If we've reached the end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps

def gas_station(gas, cost):
    """LC 134: Gas Station - find starting position for circular trip"""
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    # Impossible to complete the trip
    if total_gas < total_cost:
        return -1
    
    current_gas = 0
    start = 0
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        # If we can't reach next station from current start
        if current_gas < 0:
            current_gas = 0
            start = i + 1  # Try starting from next station
    
    return start

def container_with_most_water(height):
    """LC 11: Container With Most Water"""
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        
        # Greedy choice: move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

### **Pattern 4: Frequency/Counting Greedy**
```python
def task_scheduler(tasks, n):
    """LC 621: Task Scheduler"""
    from collections import Counter
    import heapq
    
    # Count frequency of each task
    task_counts = Counter(tasks)
    
    # Max heap of frequencies (use negative for max heap)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    time = 0
    
    while max_heap:
        cycle = []
        
        # Try to schedule tasks for one cooling cycle
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count < -1:  # Still has remaining tasks
                    cycle.append(count + 1)
        
        # Add back tasks that still need to be scheduled
        for count in cycle:
            heapq.heappush(max_heap, count)
        
        # Add time for this cycle
        time += (n + 1) if max_heap else len(cycle)
    
    return time

def task_scheduler_optimized(tasks, n):
    """Optimized mathematical approach"""
    from collections import Counter
    
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_count = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Calculate minimum time needed
    # (max_freq - 1) * (n + 1) + max_count is the minimum time
    # when we can perfectly arrange tasks with cooling periods
    min_time = (max_freq - 1) * (n + 1) + max_count
    
    # We need at least len(tasks) time to complete all tasks
    return max(len(tasks), min_time)

def reorganize_string(s):
    """LC 767: Reorganize String"""
    from collections import Counter
    import heapq
    
    # Count frequencies
    counter = Counter(s)
    
    # Check if reorganization is possible
    max_freq = max(counter.values())
    if max_freq > (len(s) + 1) // 2:
        return ""
    
    # Max heap of (frequency, character)
    max_heap = [(-freq, char) for char, freq in counter.items()]
    heapq.heapify(max_heap)
    
    result = []
    prev_freq, prev_char = 0, ''
    
    while max_heap:
        # Get most frequent character
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        
        # Add back previous character if it still has frequency
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        
        # Update previous character info
        prev_freq, prev_char = freq + 1, char
    
    return ''.join(result) if len(result) == len(s) else ""
```

### **Pattern 5: Mathematical Greedy**
```python
def candy_distribution(ratings):
    """LC 135: Candy"""
    n = len(ratings)
    candies = [1] * n
    
    # Left to right pass: ensure right neighbor with higher rating gets more candy
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # Right to left pass: ensure left neighbor with higher rating gets more candy
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    return sum(candies)

def fractional_knapsack(items, capacity):
    """Classic fractional knapsack problem"""
    # items = [(value, weight), ...]
    
    # Sort by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0
    
    for value, weight in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take fraction of the item
            total_value += value * (capacity / weight)
            break
    
    return total_value

def minimum_platforms(arrivals, departures):
    """Minimum railway platforms needed"""
    # Sort arrival and departure times
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i = j = 0
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1
    
    return max_platforms

def minimum_cost_to_connect_sticks(sticks):
    """LC 1167: Minimum Cost to Connect Sticks"""
    import heapq
    
    if len(sticks) <= 1:
        return 0
    
    # Use min heap
    heapq.heapify(sticks)
    total_cost = 0
    
    while len(sticks) > 1:
        # Take two smallest sticks
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        
        # Cost to connect them
        cost = first + second
        total_cost += cost
        
        # Put the combined stick back
        heapq.heappush(sticks, cost)
    
    return total_cost
```

### **Pattern 6: Greedy Graph Algorithms**
```python
def minimum_spanning_tree_kruskal(n, edges):
    """Kruskal's algorithm for MST"""
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1
            return True
    
    # Sort edges by weight (greedy choice)
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_cost = 0
    edges_used = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_cost += weight
            edges_used += 1
            if edges_used == n - 1:  # MST complete
                break
    
    return mst_cost

def dijkstra_shortest_path(graph, start):
    """Dijkstra's algorithm - greedy shortest path"""
    import heapq
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

## 📊 **Greedy Algorithm Analysis**

| Problem Type | Time Complexity | Space Complexity | Key Insight |
|--------------|----------------|------------------|-------------|
| **Interval Scheduling** | O(N log N) | O(1) | Sort by end time |
| **Stock Trading** | O(N) | O(1) | Capture every profit |
| **Jump Game** | O(N) | O(1) | Track farthest reachable |
| **Task Scheduling** | O(N log N) | O(N) | Process highest frequency first |
| **MST (Kruskal's)** | O(E log E) | O(V) | Sort edges by weight |
| **Candy Distribution** | O(N) | O(N) | Two-pass approach |

## 🧠 **Key Insights**

### **When Greedy Works**
1. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
2. **Greedy Choice Property**: Locally optimal choice leads to globally optimal solution
3. **No need to reconsider**: Once a choice is made, it doesn't need to be changed

### **Greedy vs Other Approaches**
- **vs DP**: Greedy is faster but works only when greedy choice property holds
- **vs Backtracking**: Greedy makes one choice per step, backtracking explores all
- **vs Divide & Conquer**: Greedy processes sequentially, D&C divides problem

### **Common Greedy Strategies**
1. **Sort first**: Many problems require sorting to identify greedy choice
2. **Earliest deadline first**: For scheduling problems
3. **Largest/smallest first**: For optimization problems
4. **Ratio-based selection**: For resource allocation problems

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify greedy choice**: "At each step, I'll choose the locally optimal option"
2. **Prove greedy works**: "This choice doesn't prevent us from reaching global optimum"
3. **Handle edge cases**: "What if multiple choices seem equally good?"

### **⚡ Optimization Techniques**
- **Sort strategically**: Choose sorting criteria carefully
- **Use appropriate data structures**: Heaps for priority-based problems
- **Two-pointer technique**: For array-based greedy problems
- **Event-based processing**: For interval problems

### **🐛 Common Pitfalls**
- **Assuming greedy always works**: Verify greedy choice property
- **Wrong sorting criteria**: Choose sort key that enables greedy choice
- **Not handling ties**: Consider what to do when multiple options are equally good
- **Forgetting edge cases**: Empty arrays, single elements, etc.

## 🔍 **Problem Identification**

**Use Greedy when you see:**
- "Maximum/minimum number of..."
- "Optimal scheduling/arrangement"
- "Earliest/latest possible"
- "Activity selection"
- "Resource allocation"
- "Interval problems"
- "Task assignment"

## 📈 **Greedy Choice Patterns**

### **Sorting-Based Greedy**
- Sort by end time (interval scheduling)
- Sort by ratio (fractional knapsack)
- Sort by deadline (task scheduling)

### **Heap-Based Greedy**
- Always pick maximum/minimum (task scheduler)
- Priority-based selection (Dijkstra's)
- Frequency-based processing (Huffman coding)

### **Two-Pass Greedy**
- Left-to-right then right-to-left (candy distribution)
- Forward and backward optimization

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Stock trading problems
- Day 3-4: Jump game variants
- Day 5-7: Interval scheduling problems

### **Week 2: Intermediate**
- Day 1-3: Task scheduling and frequency problems
- Day 4-5: Array manipulation greedy
- Day 6-7: Graph-based greedy (MST, shortest path)

### **Week 3: Advanced**
- Complex optimization problems
- Multi-constraint greedy
- Proving greedy correctness
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Identify when greedy approach is optimal
- ✅ Choose correct sorting/selection criteria
- ✅ Implement efficient greedy algorithms
- ✅ Prove greedy choice property
- ✅ Handle edge cases and ties correctly

---

**Previous**: [← Back Tracking](../13_back_tracking/) | **Next**: [Intervals →](../15_intervals/)
