# Binary Search 🔍

> **Interview Frequency**: 65% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #5

## 🎯 **Core Concept**
Binary Search is a divide-and-conquer algorithm that efficiently searches sorted data in O(log n) time. Master the template and "search for answer" pattern.

## 🏢 **Company Focus**
- **Google**: Advanced binary search, search in complex conditions
- **Meta**: Search in social graphs, recommendation systems
- **Amazon**: Inventory search, delivery optimization
- **Apple**: Efficient data retrieval in large datasets
- **Microsoft**: Database indexing, search algorithms

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Basic Template | All FAANG |
| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Lower Bound | Entry Level |
| [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | Search for Answer | Google, Meta |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Modified Binary Search | All FAANG |
| [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | Peak Finding | Google, Amazon |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Lower/Upper Bound | O(log n) | O(1) |
| [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | 2D Binary Search | O(log(m*n)) | O(1) |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Rotation Point | O(log n) | O(1) |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary Search on Answer | O(n log max) | O(1) |
| [Capacity to Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Minimize Maximum | O(n log sum) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Partition-based Binary Search |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | Binary Search + Greedy |
| [Aggressive Cows](https://www.spoj.com/problems/AGGRCOW/) | Hard | Binary Search on Answer |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Binary Search Template**
```python
def binary_search(nums, target):
    """Standard binary search - find exact target"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found
```

### **Pattern 2: Lower Bound (First Occurrence)**
```python
def find_first_occurrence(nums, target):
    """Find first position where target appears"""
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_insert_position(nums, target):
    """Find position where target should be inserted"""
    left, right = 0, len(nums)  # Note: right = len(nums)
    
    while left < right:  # Note: left < right (not <=)
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # Could be the position
    
    return left
```

### **Pattern 3: Upper Bound (Last Occurrence)**
```python
def find_last_occurrence(nums, target):
    """Find last position where target appears"""
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### **Pattern 4: Binary Search on Answer**
```python
def binary_search_on_answer(nums, condition_func):
    """Template for 'search for answer' problems"""
    left, right = min_possible_answer, max_possible_answer
    
    while left < right:
        mid = left + (right - left) // 2
        
        if condition_func(mid):
            right = mid  # mid could be answer, search for smaller
        else:
            left = mid + 1  # mid is too small
    
    return left

# Example: Koko Eating Bananas
def min_eating_speed(piles, h):
    def can_finish(speed):
        return sum((pile + speed - 1) // speed for pile in piles) <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### **Pattern 5: Rotated Array Search**
```python
def search_rotated_array(nums, target):
    """Search in rotated sorted array"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def find_min_rotated(nums):
    """Find minimum in rotated sorted array"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1  # Min is in right half
        else:
            right = mid  # Min is in left half (could be mid)
    
    return nums[left]
```

## 📊 **Template Decision Guide**

| Problem Type | Template | Key Insight |
|--------------|----------|-------------|
| **Exact Search** | Standard | Find specific target |
| **Insert Position** | Lower Bound | First position ≥ target |
| **First Occurrence** | Lower Bound | Leftmost target |
| **Last Occurrence** | Upper Bound | Rightmost target |
| **Search Answer** | Binary Search on Answer | Minimize/maximize some value |
| **Rotated Array** | Modified Standard | Handle rotation point |

## 🧠 **Key Insights**

### **Why Binary Search Works**
- **Sorted property**: Can eliminate half the search space each iteration
- **Logarithmic reduction**: n → n/2 → n/4 → ... → 1
- **Invariant maintenance**: Answer always remains in search space

### **Common Binary Search Patterns**
1. **Find exact target**: Standard template
2. **Find boundary**: Lower/upper bound templates  
3. **Optimize answer**: Binary search on answer space
4. **Handle special arrays**: Rotated, 2D matrix

### **Search Space Reduction Strategy**
- **Compare with mid**: Decide which half to eliminate
- **Maintain invariants**: Ensure target remains in valid range
- **Handle edge cases**: Empty arrays, single elements

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify constraints**: "Is the array sorted? Any duplicates?"
2. **Explain approach**: "Binary search reduces O(n) to O(log n)"
3. **Handle edge cases**: "What if array is empty or has one element?"

### **⚡ Optimization Techniques**
- **Avoid overflow**: Use `left + (right - left) // 2` instead of `(left + right) // 2`
- **Choose correct template**: Different problems need different boundary handling
- **Early termination**: Return immediately when target found (if applicable)

### **🐛 Common Pitfalls**
- **Infinite loops**: Wrong boundary updates (left = mid instead of mid + 1)
- **Off-by-one errors**: Incorrect loop conditions (< vs <=)
- **Integer overflow**: In languages without automatic big integers
- **Wrong template**: Using exact search for boundary problems

## 🔍 **Problem Identification**

**Use Binary Search when you see:**
- "Sorted array" (biggest hint!)
- "Find in O(log n) time"
- "Search for target"
- "Find first/last occurrence"
- "Minimize/maximize something" (binary search on answer)
- "Rotated sorted array"

## 📈 **Complexity Analysis**

| Problem Type | Time Complexity | Space Complexity | Notes |
|--------------|----------------|------------------|-------|
| **Basic Search** | O(log n) | O(1) | Iterative implementation |
| **Range Search** | O(log n) | O(1) | Two binary searches |
| **2D Matrix** | O(log(m*n)) | O(1) | Treat as 1D array |
| **Search Answer** | O(n log k) | O(1) | k = answer range |
| **Rotated Array** | O(log n) | O(1) | Modified binary search |

## 🎯 **Binary Search Variations**

### **2D Matrix Search**
```python
def search_matrix(matrix, target):
    """Search in row and column sorted matrix"""
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
```

### **Peak Finding**
```python
def find_peak_element(nums):
    """Find any peak element in O(log n)"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid  # Peak is in left half (could be mid)
        else:
            left = mid + 1  # Peak is in right half
    
    return left
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Basic Binary Search, Search Insert Position
- Day 3-4: First Bad Version, Find First/Last Position
- Day 5-7: Search in Rotated Sorted Array

### **Week 2: Intermediate**
- Day 1-3: Find Peak Element, Search 2D Matrix
- Day 4-5: Find Minimum in Rotated Array
- Day 6-7: Koko Eating Bananas, Capacity to Ship

### **Week 3: Advanced**
- Median of Two Sorted Arrays
- Split Array Largest Sum
- Mock interview practice

## 📋 **Binary Search Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand divide and conquer principle
- [ ] Master left, right boundary handling
- [ ] Know when to use different binary search templates
- [ ] Understand "binary search on answer" pattern
- [ ] Master rotated array search techniques

### **Essential Problems** (Must Complete)
- [ ] [Binary Search](https://leetcode.com/problems/binary-search/) - Basic template
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Rotated array
- [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Minimum finding
- [ ] [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) - 2D binary search
- [ ] [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Range finding
- [ ] [Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Insertion point
- [ ] [Sqrt(x)](https://leetcode.com/problems/sqrtx/) - Mathematical binary search

### **Intermediate Problems** (Build Proficiency)
- [ ] [Find Peak Element](https://leetcode.com/problems/find-peak-element/) - Peak finding
- [ ] [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) - With duplicates
- [ ] [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) - Duplicates handling
- [ ] [Single Element in Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) - Unique element
- [ ] [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) - Binary search on answer
- [ ] [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) - Complex optimization

### **Advanced Problems** (Expert Level)
- [ ] [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) - Advanced partitioning
- [ ] [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) - Complex binary search on answer
- [ ] [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) - Optimization problem
- [ ] [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) - Precision binary search

### **Pattern Recognition** 🧠
- [ ] Identify sorted array opportunities
- [ ] Recognize "binary search on answer" problems
- [ ] Spot optimization from O(n) to O(log n)
- [ ] Know when array rotation suggests binary search
- [ ] Understand range query optimizations

### **Implementation Skills** 💻
- [ ] Master template to avoid infinite loops
- [ ] Handle boundary conditions correctly
- [ ] Implement both iterative and recursive versions
- [ ] Use correct comparison operators (<=, <, >=, >)
- [ ] Handle integer overflow in mid calculation

### **Interview Performance** 🎯
- [ ] Solve basic binary search in under 2 minutes
- [ ] Explain why binary search works
- [ ] Choose correct template for problem type
- [ ] Handle edge cases (empty array, single element)
- [ ] Debug boundary condition issues quickly

### **Progress Tracking**
- [ ] **Problems Solved**: ___/16+ problems completed
- [ ] **Time Investment**: ___/18+ hours practiced
- [ ] **Mock Interviews**: ___/2 binary search focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Choose correct template for different problem types
- ✅ Handle boundary conditions without infinite loops
- ✅ Recognize "binary search on answer" pattern
- ✅ Optimize brute force O(n) to O(log n)
- ✅ Explain why binary search works

---

**Previous**: [← Stack & Queue](../04_stack_and_queue/) | **Next**: [Linked Lists →](../06_linked_lists/)
