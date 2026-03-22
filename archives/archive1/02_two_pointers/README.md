# Two Pointers 👉👈

> **Interview Frequency**: 80% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #2

## 🎯 **Core Concept**
Two Pointers technique optimizes O(n²) brute force solutions to O(n) by using strategic pointer movement on sorted arrays or strings.

## 🏢 **Company Focus**
- **Tech Giants**: Advanced two-pointer with complex conditions
- **Social Platforms**: String palindrome and matching problems
- **E-commerce**: Container/water trapping optimization
- **Device Manufacturers**: Clean pointer manipulation
- **Software Companies**: Array optimization problems

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Easy | Basic Two Pointers | All Companies |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Opposite Direction | Top Companies |
| [3Sum](https://leetcode.com/problems/3sum/) | Medium | Fixed + Two Pointers | Top Companies |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Greedy Two Pointers | All Companies |
| [Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | Same Direction | Entry Level |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | Target Optimization | O(n²) | O(1) |
| [4Sum](https://leetcode.com/problems/4sum/) | Medium | Nested Two Pointers | O(n³) | O(1) |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Height Array Processing | O(n) | O(1) |
| [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Dutch National Flag | O(n) | O(1) |
| [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | In-place Partitioning | O(n) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Sliding Window + Two Pointers |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand Around Centers |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | Multiple Center Expansion |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Opposite Direction (Convergent)**
```python
def two_pointers_convergent(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]

# Example: Two Sum II - Input array is sorted
def two_sum_ii(numbers, target):
    return two_pointers_convergent(numbers, target)
```

### **Pattern 2: Same Direction (Fast & Slow)**
```python
def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # Length of unique array
```

### **Pattern 3: Three Pointers (Dutch National Flag)**
```python
def sort_colors(nums):
    """Sort array with only 0s, 1s, 2s"""
    left = 0      # Next position for 0
    right = len(nums) - 1  # Next position for 2
    current = 0   # Current examination pointer
    
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[right], nums[current] = nums[current], nums[right]
            right -= 1
            # Don't increment current - need to check swapped element
        else:  # nums[current] == 1
            current += 1
```

### **Pattern 4: Expand Around Centers**
```python
def expand_around_center(s, left, right):
    """Helper function to expand palindrome around center"""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindrome(s):
    longest = ""
    
    for i in range(len(s)):
        # Odd length palindromes (center is single character)
        palindrome1 = expand_around_center(s, i, i)
        # Even length palindromes (center is between characters)
        palindrome2 = expand_around_center(s, i, i + 1)
        
        # Update longest
        for p in [palindrome1, palindrome2]:
            if len(p) > len(longest):
                longest = p
    
    return longest
```

## 📊 **When to Use Each Pattern**

| Pattern | Use Case | Example Problems |
|---------|----------|------------------|
| **Opposite Direction** | Sorted arrays, target sums | Two Sum II, 3Sum |
| **Same Direction** | Remove duplicates, partitioning | Remove Duplicates, Move Zeroes |
| **Three Pointers** | Partitioning into 3 groups | Sort Colors, Quick Sort Partition |
| **Expand Centers** | Palindrome problems | Longest Palindromic Substring |

## 🧠 **Key Insights**

### **Why Two Pointers Works**
- **Eliminates redundant comparisons**: Instead of checking all O(n²) pairs
- **Leverages sorted order**: Can make decisions about which pointer to move
- **Space optimization**: Often achieves O(1) space vs O(n) for hash map solutions

### **Decision Making for Pointer Movement**
- **Sum too small**: Move left pointer right (increase sum)
- **Sum too large**: Move right pointer left (decrease sum)
- **Condition not met**: Move appropriate pointer based on logic

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Explain why two pointers works**: "Since array is sorted, we can eliminate half the search space"
2. **Clarify pointer movement**: "If sum is too small, we need to increase it by moving left pointer"
3. **Mention space optimization**: "This avoids the O(n) space of a hash map solution"

### **⚡ Optimization Techniques**
- **Skip duplicates**: Avoid redundant iterations
- **Early termination**: Break when impossible to find solution
- **Preprocessing**: Sort array if not already sorted

### **🐛 Common Pitfalls**
- **Infinite loops**: Ensure pointers always move towards termination
- **Array bounds**: Check left < right condition
- **Duplicate handling**: Skip same values to avoid duplicate solutions
- **Sorted assumption**: Verify if array needs to be sorted first

## 🔍 **Problem Identification**

**Use Two Pointers when you see:**
- "Find pair/triplet with target sum"
- "Remove duplicates from sorted array"
- "Check if string is palindrome"
- "Partition array based on condition"
- "Container/water problems"
- "Array is sorted" (big hint!)

## 📈 **Complexity Analysis**

| Pattern | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| **Opposite Direction** | O(n) | O(1) | Single pass through array |
| **Same Direction** | O(n) | O(1) | Each element visited once |
| **Three Pointers** | O(n) | O(1) | Linear partitioning |
| **Expand Centers** | O(n²) | O(1) | n centers, each can expand n times |

## 🎭 **Pattern Variations**

### **Multi-Sum Problems**
```python
def three_sum(nums, target):
    nums.sort()  # O(n log n)
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Two Sum II, Valid Palindrome
- Day 3-4: Remove Duplicates, Move Zeroes
- Day 5-7: Container With Most Water

### **Week 2: Intermediate**
- Day 1-3: 3Sum, 3Sum Closest
- Day 4-5: Sort Colors, 4Sum
- Day 6-7: Review and edge cases

### **Week 3: Advanced**
- Trapping Rain Water
- Longest Palindromic Substring  
- Mock interview practice

## 📋 **Two Pointers Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand opposite direction (convergent) pointers
- [ ] Master same direction (chase) pointers  
- [ ] Know when two pointers beats hash map
- [ ] Understand sorted array optimization
- [ ] Master in-place array manipulation

### **Essential Problems** (Must Complete)
- [ ] [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) - Basic convergent pointers
- [ ] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - String validation
- [ ] [3Sum](https://leetcode.com/problems/3sum/) - Fixed + moving pointers
- [ ] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) - Greedy optimization
- [ ] [Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Same direction
- [ ] [Move Zeroes](https://leetcode.com/problems/move-zeroes/) - In-place partitioning
- [ ] [Sort Colors](https://leetcode.com/problems/sort-colors/) - Dutch National Flag

### **Intermediate Problems** (Build Proficiency)
- [ ] [3Sum Closest](https://leetcode.com/problems/3sum-closest/) - Target optimization
- [ ] [4Sum](https://leetcode.com/problems/4sum/) - Nested two pointers
- [ ] [Remove Element](https://leetcode.com/problems/remove-element/) - Element removal
- [ ] [Squares of Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) - Merge technique
- [ ] [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) - Reverse processing

### **Advanced Problems** (Expert Level)
- [ ] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Height processing
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Sliding window hybrid
- [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Expand around centers
- [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) - Multiple expansions

### **Pattern Recognition** 🧠
- [ ] Identify when sorted array suggests two pointers
- [ ] Recognize palindrome checking opportunities
- [ ] Spot in-place optimization potential
- [ ] Know when two pointers beats O(n²) brute force
- [ ] Understand pointer movement conditions

### **Implementation Skills** 💻
- [ ] Handle edge cases (empty arrays, single elements)
- [ ] Implement both convergent and chase patterns
- [ ] Optimize space complexity to O(1)
- [ ] Handle duplicate values correctly
- [ ] Code clean pointer movement logic

### **Interview Performance** 🎯
- [ ] Solve Two Sum II in under 2 minutes
- [ ] Explain pointer movement rationale clearly
- [ ] Handle follow-up questions confidently
- [ ] Choose optimal approach (two pointers vs hash map)
- [ ] Debug pointer boundary issues quickly

### **Progress Tracking**
- [ ] **Problems Solved**: ___/15+ problems completed
- [ ] **Time Investment**: ___/15+ hours practiced
- [ ] **Mock Interviews**: ___/2 two-pointers focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Identify when to use two pointers vs hash map
- ✅ Handle duplicate values correctly
- ✅ Optimize space from O(n) to O(1)
- ✅ Explain pointer movement logic clearly
- ✅ Solve 3Sum in under 10 minutes

---

**Previous**: [← Arrays & Hashing](../01_arrays_and_hashing/) | **Next**: [Sliding Window →](../03_sliding_window/)
