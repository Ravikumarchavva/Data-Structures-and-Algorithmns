# Intervals 📅

> **Interview Frequency**: 60% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #15

## 🎯 **Core Concept**
Interval problems involve working with ranges of values, often requiring operations like merging overlapping intervals, finding intersections, or scheduling non-conflicting activities.

## 🏢 **Company Focus**
- **Google**: Calendar scheduling, resource booking
- **Meta**: Event management, ad slot allocation
- **Amazon**: Delivery time windows, warehouse scheduling
- **Apple**: Meeting rooms, device availability windows
- **Netflix**: Content streaming windows, server maintenance
- **Microsoft**: Meeting scheduling, resource allocation

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Merge Overlapping | All FAANG |
| [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Insert & Merge | Google, Meta |
| [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Remove Minimum | Amazon, Apple |
| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | Basic Overlap Check | All FAANG |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Resource Allocation | All FAANG |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium | Two Pointers | O(M + N) | O(1) |
| [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Merge + Gap Finding | O(N log N) | O(N) |
| [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | Overlap Detection | O(N²) / O(N log N) | O(N) |
| [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | Differential Array | O(N log N) | O(N) |
| [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Medium | Sorting + Coverage | O(N log N) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | Sweep Line + Priority Queue |
| [Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/) | Hard | Segment Tree / Union-Find |
| [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | Hard | Dynamic Interval Management |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Merge Overlapping Intervals**
```python
def merge_intervals(intervals):
    """LC 56: Merge Intervals"""
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:  # Overlapping
            # Merge intervals
            last[1] = max(last[1], current[1])
        else:
            # Non-overlapping, add new interval
            merged.append(current)
    
    return merged

def merge_intervals_optimized(intervals):
    """Memory-optimized version"""
    if not intervals:
        return []
    
    intervals.sort()
    result = []
    start, end = intervals[0]
    
    for i in range(1, len(intervals)):
        curr_start, curr_end = intervals[i]
        
        if curr_start <= end:  # Overlapping
            end = max(end, curr_end)
        else:  # Non-overlapping
            result.append([start, end])
            start, end = curr_start, curr_end
    
    # Add the last interval
    result.append([start, end])
    return result

def insert_interval(intervals, new_interval):
    """LC 57: Insert Interval"""
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that end before new interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

def insert_interval_binary_search(intervals, new_interval):
    """Binary search optimized version"""
    import bisect
    
    if not intervals:
        return [new_interval]
    
    # Find insertion points
    start_pos = bisect.bisect_left(intervals, [new_interval[0], 0])
    end_pos = bisect.bisect_right(intervals, [new_interval[1], float('inf')])
    
    # Check for overlaps and merge
    if start_pos > 0 and intervals[start_pos - 1][1] >= new_interval[0]:
        start_pos -= 1
    
    merged_start = new_interval[0]
    merged_end = new_interval[1]
    
    for i in range(start_pos, min(end_pos, len(intervals))):
        if intervals[i][0] <= new_interval[1]:
            merged_start = min(merged_start, intervals[i][0])
            merged_end = max(merged_end, intervals[i][1])
    
    # Build result
    result = intervals[:start_pos]
    result.append([merged_start, merged_end])
    result.extend(intervals[end_pos:])
    
    return result
```

### **Pattern 2: Interval Intersection Problems**
```python
def interval_intersection(first_list, second_list):
    """LC 986: Interval List Intersections"""
    result = []
    i = j = 0
    
    while i < len(first_list) and j < len(second_list):
        # Find intersection
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])
        
        if start <= end:  # Valid intersection
            result.append([start, end])
        
        # Move pointer of interval that ends first
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    
    return result

def intervals_intersection_multiple_lists(interval_lists):
    """Find intersection of multiple interval lists"""
    if not interval_lists:
        return []
    
    # Start with first list
    result = interval_lists[0]
    
    # Intersect with each subsequent list
    for intervals in interval_lists[1:]:
        result = interval_intersection(result, intervals)
        if not result:  # No intersection possible
            break
    
    return result

def remove_covered_intervals(intervals):
    """LC 1288: Remove Covered Intervals"""
    if not intervals:
        return 0
    
    # Sort by start time, then by end time in descending order
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    count = 0
    prev_end = 0
    
    for start, end in intervals:
        # If current interval is not covered by previous
        if end > prev_end:
            count += 1
            prev_end = end
    
    return count

def check_intervals_overlap(interval1, interval2):
    """Check if two intervals overlap"""
    return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])

def intervals_union(intervals):
    """Find union of all intervals"""
    if not intervals:
        return []
    
    intervals.sort()
    result = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:  # Overlapping or adjacent
            current_end = max(current_end, end)
        else:  # Gap found
            result.append([current_start, current_end])
            current_start, current_end = start, end
    
    result.append([current_start, current_end])
    return result
```

### **Pattern 3: Meeting Room Problems**
```python
def can_attend_meetings(intervals):
    """LC 252: Meeting Rooms"""
    if not intervals:
        return True
    
    intervals.sort()
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:  # Overlap
            return False
    
    return True

def min_meeting_rooms(intervals):
    """LC 253: Meeting Rooms II - Using heap"""
    if not intervals:
        return 0
    
    import heapq
    
    intervals.sort()  # Sort by start time
    heap = []  # Min heap to track end times
    
    for start, end in intervals:
        # Remove meetings that have ended
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)

def min_meeting_rooms_events(intervals):
    """Alternative solution using event-based approach"""
    if not intervals:
        return 0
    
    events = []
    
    for start, end in intervals:
        events.append((start, 1))    # Meeting starts
        events.append((end, -1))     # Meeting ends
    
    # Sort by time, prioritize end events before start events
    events.sort(key=lambda x: (x[0], x[1]))
    
    concurrent_meetings = 0
    max_rooms = 0
    
    for time, event_type in events:
        concurrent_meetings += event_type
        max_rooms = max(max_rooms, concurrent_meetings)
    
    return max_rooms

def employee_free_time(schedule):
    """LC 759: Employee Free Time"""
    # Flatten all intervals
    all_intervals = []
    for employee_schedule in schedule:
        all_intervals.extend(employee_schedule)
    
    # Merge overlapping intervals
    merged = merge_intervals(all_intervals)
    
    # Find gaps between merged intervals
    free_time = []
    for i in range(1, len(merged)):
        if merged[i-1][1] < merged[i][0]:
            free_time.append([merged[i-1][1], merged[i][0]])
    
    return free_time
```

### **Pattern 4: Calendar and Booking Problems**
```python
class MyCalendar:
    """LC 729: My Calendar I"""
    
    def __init__(self):
        self.bookings = []
    
    def book(self, start, end):
        """Book if no overlap with existing bookings"""
        for s, e in self.bookings:
            if max(start, s) < min(end, e):  # Overlap condition
                return False
        
        self.bookings.append((start, end))
        return True

class MyCalendarOptimized:
    """Optimized with binary search"""
    
    def __init__(self):
        self.bookings = []
    
    def book(self, start, end):
        import bisect
        
        # Find position where (start, end) should be inserted
        pos = bisect.bisect_left(self.bookings, (start, end))
        
        # Check overlap with previous booking
        if pos > 0 and self.bookings[pos-1][1] > start:
            return False
        
        # Check overlap with next booking
        if pos < len(self.bookings) and self.bookings[pos][0] < end:
            return False
        
        # Insert booking at correct position
        self.bookings.insert(pos, (start, end))
        return True

class MyCalendarTwo:
    """LC 731: My Calendar II - Allow at most 2 overlaps"""
    
    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []
    
    def book(self, start, end):
        # Check if triple booking would occur
        for s, e in self.double_bookings:
            if max(start, s) < min(end, e):
                return False
        
        # Add overlaps with single bookings to double bookings
        for s, e in self.single_bookings:
            overlap_start = max(start, s)
            overlap_end = min(end, e)
            if overlap_start < overlap_end:
                self.double_bookings.append((overlap_start, overlap_end))
        
        self.single_bookings.append((start, end))
        return True

class MyCalendarThree:
    """LC 732: My Calendar III - Maximum overlaps"""
    
    def __init__(self):
        self.events = {}
    
    def book(self, start, end):
        # Use differential array approach
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        
        # Calculate maximum overlaps
        active = 0
        max_overlaps = 0
        
        for time in sorted(self.events.keys()):
            active += self.events[time]
            max_overlaps = max(max_overlaps, active)
        
        return max_overlaps
```

### **Pattern 5: Advanced Interval Problems**
```python
def car_pooling(trips, capacity):
    """LC 1094: Car Pooling"""
    # Use differential array
    events = []
    
    for passengers, start, end in trips:
        events.append((start, passengers))    # Pick up
        events.append((end, -passengers))     # Drop off
    
    events.sort()
    current_passengers = 0
    
    for location, change in events:
        current_passengers += change
        if current_passengers > capacity:
            return False
    
    return True

def minimum_arrows_burst_balloons(points):
    """LC 452: Minimum Number of Arrows to Burst Balloons"""
    if not points:
        return 0
    
    # Sort by end position
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    arrow_position = points[0][1]
    
    for start, end in points[1:]:
        if start > arrow_position:  # Need new arrow
            arrows += 1
            arrow_position = end
    
    return arrows

def non_overlapping_intervals(intervals):
    """LC 435: Non-overlapping Intervals"""
    if not intervals:
        return 0
    
    # Sort by end time (greedy approach)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:  # Overlapping
            count += 1  # Remove current interval
        else:
            last_end = intervals[i][1]
    
    return count

def partition_labels(s):
    """LC 763: Partition Labels (interval-based thinking)"""
    # Find last occurrence of each character
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    result = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        
        if i == end:  # Reached end of current partition
            result.append(end - start + 1)
            start = i + 1
    
    return result

class SummaryRanges:
    """LC 352: Data Stream as Disjoint Intervals"""
    
    def __init__(self):
        self.intervals = []
    
    def addNum(self, val):
        import bisect
        
        # Find insertion position
        pos = bisect.bisect_left(self.intervals, [val, val])
        
        # Check for merge opportunities
        start, end = val, val
        
        # Merge with previous interval if possible
        if pos > 0 and self.intervals[pos-1][1] >= val - 1:
            pos -= 1
            start = self.intervals[pos][0]
        
        # Merge with subsequent intervals
        while pos < len(self.intervals) and self.intervals[pos][0] <= end + 1:
            end = max(end, self.intervals[pos][1])
            self.intervals.pop(pos)
        
        # Insert merged interval
        self.intervals.insert(pos, [start, end])
    
    def getIntervals(self):
        return self.intervals
```

### **Pattern 6: Sweep Line Algorithm**
```python
def min_interval_to_include_query(intervals, queries):
    """LC 1851: Minimum Interval to Include Each Query"""
    import heapq
    
    # Sort intervals by start time
    intervals.sort()
    # Create queries with indices for result mapping
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    
    result = [-1] * len(queries)
    min_heap = []  # (length, end)
    interval_idx = 0
    
    for query, original_idx in sorted_queries:
        # Add all intervals that start at or before query
        while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
            start, end = intervals[interval_idx]
            heapq.heappush(min_heap, (end - start + 1, end))
            interval_idx += 1
        
        # Remove intervals that end before query
        while min_heap and min_heap[0][1] < query:
            heapq.heappop(min_heap)
        
        # Get minimum interval length that includes query
        if min_heap:
            result[original_idx] = min_heap[0][0]
    
    return result

def rectangle_area(rectangles):
    """LC 850: Rectangle Area II (sweep line)"""
    events = []
    
    # Create events for vertical lines
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))    # Rectangle starts
        events.append((x2, y1, y2, -1))   # Rectangle ends
    
    events.sort()
    
    def merge_intervals(intervals):
        if not intervals:
            return []
        
        intervals.sort()
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        
        return merged
    
    total_area = 0
    active_intervals = []
    
    for i in range(len(events)):
        x, y1, y2, delta = events[i]
        
        # Calculate area with current active intervals
        if i > 0:
            width = x - events[i-1][0]
            merged = merge_intervals(active_intervals)
            height = sum(end - start for start, end in merged)
            total_area += width * height
        
        # Update active intervals
        if delta == 1:
            active_intervals.append((y1, y2))
        else:
            active_intervals.remove((y1, y2))
    
    return total_area % (10**9 + 7)
```

## 📊 **Interval Algorithm Complexity**

| Problem Type | Time Complexity | Space Complexity | Key Technique |
|--------------|----------------|------------------|---------------|
| **Merge Intervals** | O(N log N) | O(1) | Sort + Single Pass |
| **Insert Interval** | O(N) | O(1) | Three-phase Processing |
| **Meeting Rooms II** | O(N log N) | O(N) | Min Heap or Events |
| **Interval Intersection** | O(M + N) | O(1) | Two Pointers |
| **Calendar Booking** | O(N²) / O(N log N) | O(N) | Linear/Binary Search |
| **Sweep Line** | O(N log N) | O(N) | Event Processing |

## 🧠 **Key Insights**

### **Common Interval Operations**
1. **Overlap Detection**: `max(start1, start2) < min(end1, end2)`
2. **Merge Condition**: `start2 <= end1`
3. **Coverage**: `start1 <= start2 && end2 <= end1`
4. **Gap Detection**: `end1 < start2`

### **Sorting Strategies**
- **By start time**: For merging, basic processing
- **By end time**: For greedy scheduling problems
- **By length**: For optimization problems
- **Custom comparators**: For complex requirements

### **Data Structure Choices**
- **Array sorting**: For most merge/intersection problems
- **Heap**: For dynamic scheduling (meeting rooms)
- **TreeMap/BST**: For efficient calendar implementations
- **Differential array**: For range update problems

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify interval representation**: Open/closed intervals, edge cases
2. **Discuss sorting strategy**: Why sort by start vs end time
3. **Explain overlap conditions**: Clear mathematical conditions

### **⚡ Optimization Techniques**
- **Early termination**: Stop when no more overlaps possible
- **Binary search**: For insertion and lookup operations
- **Event-based processing**: For complex scheduling problems
- **Lazy evaluation**: Process only when needed

### **🐛 Common Pitfalls**
- **Off-by-one errors**: Careful with boundary conditions
- **Empty interval handling**: Check for edge cases
- **Sorting stability**: Consider when intervals have same start/end
- **Memory optimization**: In-place vs extra space tradeoffs

## 🔍 **Problem Identification**

**Use Interval Patterns when you see:**
- "Meeting rooms/scheduling"
- "Merge overlapping..."
- "Find intersections"
- "Minimum intervals to remove"
- "Calendar booking"
- "Time ranges/windows"
- "Resource allocation over time"

## 📈 **Template Selection Guide**

### **Choose Based on Problem Type:**
1. **Merge/Union**: Sort by start time, single pass
2. **Intersection**: Two pointers on sorted lists
3. **Scheduling**: Sort by end time (greedy)
4. **Dynamic booking**: Heap or balanced BST
5. **Range queries**: Sweep line algorithm
6. **Gap finding**: Sort and check consecutive intervals

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Merge Intervals, Insert Interval
- Day 3-4: Meeting Rooms I & II
- Day 5-7: Interval intersection problems

### **Week 2: Intermediate**
- Day 1-3: Calendar booking problems
- Day 4-5: Greedy interval scheduling
- Day 6-7: Advanced merge and coverage problems

### **Week 3: Advanced**
- Sweep line algorithms
- Dynamic interval management
- Complex optimization problems
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Master overlap detection and merging
- ✅ Choose optimal sorting strategies
- ✅ Implement efficient calendar systems
- ✅ Handle edge cases correctly
- ✅ Optimize for different constraints

---

**Previous**: [← Greedy](../14_greedy/) | **Next**: [Math & Geometry →](../16_math_and_geometry/)
