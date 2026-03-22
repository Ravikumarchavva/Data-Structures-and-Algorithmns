# Sliding Window 🔄

> **Interview Frequency**: 75% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #3

## 🎯 **Core Concept**
Sliding Window optimizes problems involving contiguous subarrays/substrings by maintaining a window that expands and contracts based on conditions, reducing O(n²) to O(n).

## 🏢 **Company Focus**
- **Tech Giants**: Complex window conditions, streaming data
- **Social Platforms**: Content filtering, user engagement windows
- **E-commerce**: Delivery time windows, inventory management
- **Device Manufacturers**: Performance monitoring, user session tracking
- **Streaming Services**: Streaming buffer optimization, view time analysis

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Fixed Window | All Entry Level |
| [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Fixed Window | Google, Amazon |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Variable Window | All FAANG |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Variable Window | All FAANG |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Fixed Window + Deque | Google, Amazon |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Frequency + K operations | O(n) | O(1) |
| [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed size + frequency match | O(n) | O(1) |
| [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | Fixed window anagram detection | O(n) | O(1) |
| [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | At most 2 distinct elements | O(n) | O(1) |
| [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Medium | Product constraint | O(n) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hard | Multiple word matching |
| [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | Hard | Sliding Window + Greedy |
| [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | Exactly K = At Most K - At Most (K-1) |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Fixed Size Window**
```python
def max_average_subarray(nums, k):
    """Find maximum average of subarray of size k"""
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        # Slide window: remove leftmost, add rightmost
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k

def sliding_window_maximum(nums, k):
    """Maximum in each window of size k using deque"""
    from collections import deque
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (they won't be maximum)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### **Pattern 2: Variable Size Window (Expand/Contract)**
```python
def longest_substring_without_repeating(s):
    """Longest substring with unique characters"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Contract window while we have duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Expand window
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def min_window_substring(s, t):
    """Minimum window substring containing all characters of t"""
    if not s or not t:
        return ""
    
    # Character frequency in t
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)  # Number of unique chars in t
    formed = 0  # Number of unique chars in current window with desired frequency
    
    window_counts = {}
    left = right = 0
    
    # (window length, left, right)
    ans = (float("inf"), None, None)
    
    while right < len(s):
        # Expand window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Contract window while it's valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update answer if this window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Contract from left
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

### **Pattern 3: At Most K Pattern**
```python
def longest_substring_with_at_most_k_distinct(s, k):
    """Longest substring with at most k distinct characters"""
    if k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Expand window
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        
        # Contract window if more than k distinct
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def subarrays_with_at_most_k_distinct(nums, k):
    """Count subarrays with at most k distinct integers"""
    def at_most_k(k):
        count = {}
        left = 0
        result = 0
        
        for right in range(len(nums)):
            if nums[right] not in count:
                count[nums[right]] = 0
            count[nums[right]] += 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1  # All subarrays ending at right
        
        return result
    
    return at_most_k(k) - at_most_k(k - 1)  # Exactly k = at_most_k - at_most_(k-1)
```

### **Pattern 4: Character Frequency Matching**
```python
def find_anagrams(s, p):
    """Find all anagrams of p in s"""
    if len(p) > len(s):
        return []
    
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
    
    window_count = {}
    result = []
    window_size = len(p)
    
    for i in range(len(s)):
        # Expand window
        char = s[i]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Contract window if size exceeds p
        if i >= window_size:
            left_char = s[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - window_size + 1)
    
    return result

def check_inclusion(s1, s2):
    """Check if s2 contains permutation of s1"""
    if len(s1) > len(s2):
        return False
    
    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    
    window_count = {}
    window_size = len(s1)
    
    for i in range(len(s2)):
        # Expand window
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Contract window
        if i >= window_size:
            left_char = s2[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        # Check match
        if window_count == s1_count:
            return True
    
    return False
```

## 📊 **Window Type Decision Guide**

| Problem Characteristics | Window Type | Template |
|------------------------|-------------|----------|
| **Fixed size mentioned** | Fixed Window | Slide by 1, maintain size |
| **"At most K"** | Variable Window | Expand until invalid, then contract |
| **"Exactly K"** | At Most K pattern | at_most(K) - at_most(K-1) |
| **Optimize some metric** | Variable Window | Expand while valid, contract to optimize |
| **Frequency matching** | Fixed/Variable | Use frequency maps |

## 🧠 **Key Insights**

### **Why Sliding Window Works**
- **Avoid recomputation**: Don't recalculate entire window each time
- **Maintain invariants**: Window always satisfies certain properties
- **Two-pointer optimization**: Left and right pointers move efficiently

### **Window State Management**
- **Expansion**: Add new element to window (right pointer)
- **Contraction**: Remove element from window (left pointer)  
- **Validation**: Check if current window satisfies conditions

### **Common Optimizations**
- **Early termination**: Stop when optimal solution found
- **Frequency maps**: Track character/element counts efficiently
- **Deque for extrema**: Maintain max/min in sliding window

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify pattern**: "This looks like a sliding window problem"
2. **Choose window type**: "Since we need at most K, I'll use variable window"
3. **Explain expansion/contraction**: "Expand while valid, contract when invalid"

### **⚡ Optimization Techniques**
- **Use frequency maps**: Avoid nested loops for character counting
- **Minimize window operations**: Only update when necessary
- **Handle edge cases**: Empty arrays, single elements

### **🐛 Common Pitfalls**
- **Off-by-one errors**: Window size calculation mistakes
- **Infinite loops**: Ensure progress in contraction phase
- **Memory leaks**: Remove elements from frequency maps when count becomes 0
- **Wrong window bounds**: Inclusive vs exclusive boundaries

## 🔍 **Problem Identification**

**Use Sliding Window when you see:**
- "Subarray" or "substring" with constraints
- "Contiguous elements"
- "Maximum/minimum in windows of size K"
- "At most/exactly K distinct elements"
- "Optimize something over all windows"

## 📈 **Complexity Analysis**

| Window Type | Time Complexity | Space Complexity | Notes |
|-------------|----------------|------------------|-------|
| **Fixed Window** | O(n) | O(1) or O(k) | Each element visited twice max |
| **Variable Window** | O(n) | O(k) | k = window size or distinct elements |
| **Frequency Matching** | O(n) | O(alphabet) | Usually O(26) for lowercase letters |
| **Deque-based** | O(n) | O(k) | For sliding window maximum/minimum |

## 🎯 **Advanced Patterns**

### **Sliding Window with Complex Conditions**
```python
def character_replacement(s, k):
    """Longest substring with at most k character replacements"""
    char_count = {}
    left = 0
    max_length = 0
    max_freq = 0
    
    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        max_freq = max(max_freq, char_count[char])
        
        # If window size - most frequent char > k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            left_char = s[left]
            char_count[left_char] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### **Multiple Windows Simultaneously**
```python
def max_sum_two_non_overlapping_subarrays(nums, first_len, second_len):
    """Maximum sum of two non-overlapping subarrays"""
    def max_sum_with_one_subarray(nums, len1, len2):
        # Calculate max sum ending before or at each position
        sum1 = sum(nums[:len1])
        max_sum1 = sum1
        max_ending_here = [0] * len(nums)
        max_ending_here[len1 - 1] = sum1
        
        for i in range(len1, len(nums) - len2):
            sum1 += nums[i] - nums[i - len1]
            max_sum1 = max(max_sum1, sum1)
            max_ending_here[i] = max_sum1
        
        # Calculate max sum of second subarray
        sum2 = sum(nums[len1:len1 + len2])
        result = max_ending_here[len1 - 1] + sum2
        
        for i in range(len1 + len2, len(nums)):
            sum2 += nums[i] - nums[i - len2]
            result = max(result, max_ending_here[i - len2] + sum2)
        
        return result
    
    return max(max_sum_with_one_subarray(nums, first_len, second_len),
               max_sum_with_one_subarray(nums, second_len, first_len))
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Fixed size windows (max average, sliding window max)
- Day 3-4: Basic variable windows (longest substring without repeating)
- Day 5-7: At most K problems (K distinct characters)

### **Week 2: Intermediate**  
- Day 1-3: Minimum window substring, permutation in string
- Day 4-5: Find all anagrams, character replacement
- Day 6-7: Subarray product less than K

### **Week 3: Advanced**
- Substring with concatenation of all words
- Subarrays with exactly K distinct integers
- Multiple sliding windows problems
- Mock interview practice

## 📋 **Sliding Window Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand fixed vs variable window patterns
- [ ] Master expand/contract window logic
- [ ] Know when sliding window optimizes O(n²) to O(n)
- [ ] Understand frequency map usage in windows
- [ ] Master substring vs subarray problems

### **Essential Problems** (Must Complete)
- [ ] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Fixed window foundation
- [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Variable window classic
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Complex variable window
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Deque optimization
- [ ] [Permutation in String](https://leetcode.com/problems/permutation-in-string/) - Fixed window with frequency
- [ ] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Variable with K changes
- [ ] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Simple window tracking

### **Intermediate Problems** (Build Proficiency)
- [ ] [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) - Fixed window anagrams
- [ ] [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) - At most K types
- [ ] [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) - K distinct
- [ ] [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) - K flips allowed
- [ ] [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) - Exactly K distinct

### **Advanced Problems** (Expert Level)
- [ ] [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) - Multiple word matching
- [ ] [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Sum target optimization
- [ ] [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) - Count all valid
- [ ] [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) - Cost-based window

### **Pattern Recognition** 🧠
- [ ] Identify "contiguous subarray/substring" problems
- [ ] Recognize when brute force O(n²) can become O(n)
- [ ] Spot frequency counting within windows
- [ ] Know when to use fixed vs variable window
- [ ] Understand "at most K" vs "exactly K" patterns

### **Implementation Skills** 💻
- [ ] Implement both fixed and variable window templates
- [ ] Handle window expansion and contraction logic
- [ ] Use frequency maps/counters efficiently
- [ ] Optimize space complexity when possible
- [ ] Handle edge cases (empty input, K > array length)

### **Interview Performance** 🎯
- [ ] Identify sliding window pattern in problem statement
- [ ] Choose correct window type (fixed/variable)
- [ ] Implement expand/contract logic correctly
- [ ] Explain time complexity improvement clearly
- [ ] Handle follow-up questions about optimization

### **Progress Tracking**
- [ ] **Problems Solved**: ___/18+ problems completed
- [ ] **Time Investment**: ___/25+ hours practiced  
- [ ] **Mock Interviews**: ___/3 sliding window focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Distinguish between fixed and variable window problems
- ✅ Implement expand/contract logic correctly
- ✅ Use frequency maps efficiently
- ✅ Handle edge cases (empty input, single element)
- ✅ Optimize from O(n²) brute force to O(n) sliding window

---

**Previous**: [← Two Pointers](../02_two_pointers/) | **Next**: [Stack & Queue →](../04_stack_and_queue/)
