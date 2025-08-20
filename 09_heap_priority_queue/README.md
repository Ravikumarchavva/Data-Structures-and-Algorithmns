# Heap/Priority Queue 🏔️

> **Interview Frequency**: 55% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #9

## 🎯 **Core Concept**
Heaps are complete binary trees that maintain the heap property (parent ≤ children for min-heap). Priority Queues use heaps to efficiently access the minimum/maximum element in O(log n) time.

## 🏢 **Company Focus**
- **Google**: K-th element problems, streaming data processing
- **Meta**: Top posts, trending content algorithms
- **Amazon**: Order priority, delivery optimization
- **Apple**: Task scheduling, resource management
- **Netflix**: Content recommendation ranking
- **Microsoft**: Process scheduling, priority systems

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Kth Largest Element in Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Min Heap of Size K | All FAANG |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Frequency + Heap | All FAANG |
| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Min Heap for Merging | Google, Amazon |
| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Two Heaps (Max + Min) | All FAANG |
| [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | Max Heap Operations | Apple, Microsoft |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Kth Smallest Element in Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | Min Heap + Matrix Traversal | O(k log k) | O(k) |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Min Heap for End Times | O(n log n) | O(n) |
| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Max Heap + Cooling | O(n) | O(1) |
| [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | Medium | Min Heap + Generation | O(n log n) | O(n) |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Deque (not heap but similar) | O(n) | O(k) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [IPO](https://leetcode.com/problems/ipo/) | Hard | Two Heaps for Optimization |
| [Smallest Range Covering Elements](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Hard | Min Heap + Range Tracking |
| [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Merge Intervals with Heap |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Heap Operations**
```python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, val)
    
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, -val)  # Negate for max heap
    
    def pop(self):
        return -heapq.heappop(self.heap) if self.heap else None
    
    def peek(self):
        return -self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)

# Example: Kth Largest Element
def find_kth_largest(nums, k):
    """Using min heap of size k"""
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]  # Kth largest is root of min heap
```

### **Pattern 2: Top K Elements**
```python
def top_k_frequent(nums, k):
    """Top K frequent elements using heap"""
    from collections import Counter
    
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap of size k
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract elements (frequency doesn't matter for result)
    return [num for freq, num in heap]

def k_closest_points(points, k):
    """K closest points to origin"""
    # Use max heap of size k (store negative distances)
    heap = []
    
    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max heap behavior
        
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        elif dist > heap[0][0]:  # Current point is closer
            heapq.heapreplace(heap, (dist, x, y))
    
    return [[x, y] for dist, x, y in heap]
```

### **Pattern 3: Two Heaps (Median Finding)**
```python
class MedianFinder:
    """Find median from data stream using two heaps"""
    def __init__(self):
        self.small = []  # Max heap (store negative values)
        self.large = []  # Min heap
    
    def add_num(self, num):
        # Add to max heap (small) first
        heapq.heappush(self.small, -num)
        
        # Ensure all elements in small <= all elements in large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance heap sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
```

### **Pattern 4: Merge K Sorted Structures**
```python
def merge_k_sorted_lists(lists):
    """Merge k sorted linked lists using heap"""
    heap = []
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        
        # Add to result
        current.next = ListNode(val)
        current = current.next
        
        # Add next element from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

def merge_k_sorted_arrays(arrays):
    """Merge k sorted arrays"""
    heap = []
    
    # Initialize with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array_index, element_index)
    
    result = []
    
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    
    return result
```

### **Pattern 5: Meeting Rooms / Interval Scheduling**
```python
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed"""
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times of ongoing meetings
    heap = []
    
    for start, end in intervals:
        # If meeting room is available (earliest end time <= current start)
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)  # Number of ongoing meetings = rooms needed

def meeting_rooms_schedule(intervals):
    """Get the actual room assignments"""
    if not intervals:
        return []
    
    # Add index to track original intervals
    indexed_intervals = [(start, end, i) for i, (start, end) in enumerate(intervals)]
    indexed_intervals.sort()
    
    # Heap stores (end_time, room_number)
    heap = []
    room_assignments = [0] * len(intervals)
    next_room = 0
    
    for start, end, original_idx in indexed_intervals:
        if heap and heap[0][0] <= start:
            # Reuse existing room
            _, room_num = heapq.heappop(heap)
            room_assignments[original_idx] = room_num
        else:
            # Need new room
            room_assignments[original_idx] = next_room
            next_room += 1
        
        heapq.heappush(heap, (end, room_assignments[original_idx]))
    
    return room_assignments, next_room  # assignments and total rooms
```

## 📊 **Heap Operations Complexity**

| Operation | Min Heap | Max Heap | Notes |
|-----------|----------|----------|-------|
| **Insert** | O(log n) | O(log n) | Bubble up |
| **Extract Min/Max** | O(log n) | O(log n) | Bubble down |
| **Peek** | O(1) | O(1) | Root element |
| **Build Heap** | O(n) | O(n) | Heapify from array |
| **Delete Arbitrary** | O(log n) | O(log n) | If index known |

## 🧠 **Key Insights**

### **When to Use Heaps**
- **Top K problems**: Find K largest/smallest elements
- **Streaming data**: Continuous min/max queries
- **Merge operations**: Combine multiple sorted structures
- **Scheduling**: Priority-based task management
- **Median finding**: Two heaps technique

### **Heap vs Other Data Structures**
- **vs Sorting**: O(n log k) vs O(n log n) for top K
- **vs Array**: O(1) access but O(log n) for priority operations
- **vs BST**: Similar operations but heap guarantees shape

### **Common Heap Patterns**
1. **Fixed size heap**: For top K problems
2. **Two heaps**: For median/percentile problems
3. **Custom comparator**: For complex objects
4. **Heap as priority queue**: For scheduling/merging

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify pattern**: "This is a top K problem, perfect for heap"
2. **Explain choice**: "Min heap of size K gives us Kth largest efficiently"
3. **Discuss trade-offs**: "Heap gives O(log n) vs O(n) for finding min"

### **⚡ Optimization Techniques**
- **Size-limited heaps**: For top K problems (space optimization)
- **Custom comparators**: For complex objects
- **Two heaps**: For median/percentile problems
- **Lazy deletion**: Mark deleted instead of actually removing

### **🐛 Common Pitfalls**
- **Max heap simulation**: Python only has min heap (use negative values)
- **Tuple comparison**: Be careful with tie-breaking in complex objects
- **Empty heap**: Always check before popping
- **Heap property**: Don't modify elements in-place

## 🔍 **Problem Identification**

**Use Heap when you see:**
- "Top K" or "Kth largest/smallest"
- "Find median" or "percentile"
- "Merge K sorted" structures
- "Meeting rooms" or scheduling
- "Priority" or "ranking"
- "Streaming data" with min/max queries

## 📈 **Complexity Patterns**

| Problem Type | Time Complexity | Space Complexity | Notes |
|--------------|----------------|------------------|-------|
| **Top K Elements** | O(n log k) | O(k) | Better than O(n log n) sort |
| **Median Stream** | O(log n) per insert | O(n) | Two heaps approach |
| **Merge K Lists** | O(n log k) | O(k) | n = total elements |
| **Meeting Rooms** | O(n log n) | O(n) | Sorting + heap |
| **Kth in Matrix** | O(k log k) | O(k) | Better than O(n²) |

## 🎯 **Advanced Heap Applications**

### **Task Scheduler with Cooling**
```python
def least_interval(tasks, n):
    """Task scheduler with cooling period"""
    from collections import Counter
    import heapq
    
    count = Counter(tasks)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)
    
    time = 0
    queue = []  # (count, idle_time)
    
    while max_heap or queue:
        time += 1
        
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)  # Process one task
            if cnt:
                queue.append([cnt, time + n])  # Add to cooling
        
        # Check if any task finished cooling
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.pop(0)[0])
    
    return time
```

### **Sliding Window Maximum (Alternative)**
```python
def sliding_window_maximum_heap(nums, k):
    """Using heap (less efficient than deque but shows pattern)"""
    import heapq
    
    heap = []
    result = []
    
    for i, num in enumerate(nums):
        # Add current element
        heapq.heappush(heap, (-num, i))  # Max heap with index
        
        # Remove elements outside window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        # Add result if window is complete
        if i >= k - 1:
            result.append(-heap[0][0])
    
    return result
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Kth Largest Element, Last Stone Weight
- Day 3-4: Top K Frequent Elements, K Closest Points
- Day 5-7: Merge K Sorted Lists

### **Week 2: Intermediate**
- Day 1-3: Find Median from Data Stream
- Day 4-5: Meeting Rooms II, Task Scheduler
- Day 6-7: Kth Smallest in Sorted Matrix

### **Week 3: Advanced**
- IPO, Smallest Range Covering Elements
- Employee Free Time
- Custom heap implementations
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Implement min and max heaps correctly
- ✅ Solve top K problems efficiently (O(n log k) vs O(n log n))
- ✅ Use two heaps for median problems
- ✅ Apply heaps to merge and scheduling problems
- ✅ Handle custom comparators and complex objects

---

**Previous**: [← Tries](../08_tries/) | **Next**: [Backtracking →](../10_backtracking/)
