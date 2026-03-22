# Arrays & Hashing 🗃️

> **Interview Frequency**: 95% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #1

## 🎯 **Core Concept**
Arrays and Hash Maps are the foundation of most coding interviews. Master frequency counting, lookup optimization, and space-time trade-offs.

## 🏢 **Company Focus**
- **Tech Companies**: Advanced hashing, custom hash functions
- **Social Platforms**: Social graph problems using hashmaps  
- **E-commerce**: Inventory tracking, frequency analysis
- **Device Manufacturers**: Clean array manipulation
- **Streaming Services**: Recommendation frequency counting

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Hash Map Lookup | All Companies |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Frequency Counting | Top Companies |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Frequency + Heap | All Companies |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Character Frequency | Top Companies |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Set Usage | Entry Level |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix/Suffix Products | O(n) | O(1) |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Set for O(1) Lookup | O(n) | O(n) |
| [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | String Encoding | O(n) | O(1) |
| [3Sum](https://leetcode.com/problems/3sum/) | Medium | Hash + Two Pointers | O(n²) | O(1) |
| [4Sum](https://leetcode.com/problems/4sum/) | Medium | Nested Hash Tables | O(n³) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept | 
|---------|------------|------------------|
| [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | Array as Hash Table |
| [Substring with Concatenation](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hard | Sliding Window + Hash |
| [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | Merge Sort + Hash |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Frequency Counting**
```python
def frequency_pattern(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Example: Find most frequent element
def most_frequent(arr):
    freq = frequency_pattern(arr)
    return max(freq, key=freq.get)
```

### **Pattern 2: Hash Map Lookup** 
```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### **Pattern 3: Set for Duplicates**
```python
def has_duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False
```

### **Pattern 4: Array as Hash (Limited Range)**
```python
def counting_sort_approach(arr, max_val):
    # When array values are in range [0, max_val]
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    return count
```

## 📊 **Complexity Analysis**

| Operation | Array | Hash Map | Set |
|-----------|-------|----------|-----|
| **Access** | O(1) | O(1) avg | N/A |
| **Search** | O(n) | O(1) avg | O(1) avg |
| **Insert** | O(n) | O(1) avg | O(1) avg |
| **Delete** | O(n) | O(1) avg | O(1) avg |
| **Space** | O(n) | O(n) | O(n) |

## 🧠 **Key Insights**

### **When to Use Hash Maps**
- Need O(1) lookup time
- Frequency counting problems  
- Complement searching (Two Sum pattern)
- Grouping by criteria (anagrams)

### **When to Use Sets**
- Duplicate detection
- Membership testing
- Mathematical set operations

### **When to Use Arrays**
- Index-based access needed
- Limited range of values (counting sort)
- Space optimization important

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify constraints**: "What's the range of values?"
2. **Discuss trade-offs**: "HashMap uses O(n) space for O(1) lookups"
3. **Mention alternatives**: "Could also sort first, but that's O(n log n)"

### **⚡ Optimization Techniques**
- **Space optimization**: Use array instead of HashMap for limited ranges
- **Early termination**: Return immediately when condition met
- **In-place operations**: Modify input array when allowed

### **🐛 Common Pitfalls**
- Hash collisions in worst case → O(n) operations
- Integer overflow in sum problems
- Modifying collection while iterating
- Not handling edge cases (empty arrays)

## 🔍 **Problem Identification**

**Use Arrays & Hashing when you see:**
- "Find duplicates"
- "Count frequency"  
- "Group by criteria"
- "Two/Three/Four Sum"
- "Anagram problems"
- "Subarray with given sum"

## 📈 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Two Sum, Contains Duplicate
- Day 3-4: Valid Anagram, Group Anagrams  
- Day 5-7: Top K Frequent, Product of Array

### **Week 2: Intermediate**
- Day 1-3: 3Sum, Longest Consecutive Sequence
- Day 4-5: Encode/Decode Strings
- Day 6-7: Review and optimize solutions

### **Week 3: Advanced**
- First Missing Positive
- Substring with Concatenation
- Mock interview practice

## 📋 **Arrays & Hashing Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand O(1) hash table lookups
- [ ] Master frequency counting techniques
- [ ] Know when to use Array vs HashMap vs Set
- [ ] Understand hash collision handling
- [ ] Master space-time complexity trade-offs

### **Essential Problems** (Must Complete)
- [ ] [Two Sum](https://leetcode.com/problems/two-sum/) - Hash map lookup
- [ ] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) - Frequency counting
- [ ] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Frequency + heap
- [ ] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) - Prefix/suffix
- [ ] [Valid Anagram](https://leetcode.com/problems/valid-anagram/) - Character frequency
- [ ] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) - Set usage
- [ ] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) - Set optimization
- [ ] [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) - String manipulation

### **Intermediate Problems** (Build Proficiency)
- [ ] [3Sum](https://leetcode.com/problems/3sum/) - Hash + two pointers
- [ ] [4Sum](https://leetcode.com/problems/4sum/) - Nested hash tables
- [ ] [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) - Sorted array
- [ ] [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Prefix sum + hash
- [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Sliding window + hash

### **Advanced Problems** (Expert Level)
- [ ] [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) - Array as hash table
- [ ] [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) - Complex hashing
- [ ] [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) - Advanced techniques

### **Pattern Recognition** 🧠
- [ ] Instantly recognize when to use hash maps for O(1) lookup
- [ ] Identify frequency counting opportunities
- [ ] Spot space-time optimization possibilities
- [ ] Recognize when arrays can act as hash tables (limited range)

### **Implementation Skills** 💻
- [ ] Implement hash map from scratch (basic understanding)
- [ ] Code frequency counter in 3 different ways
- [ ] Handle hash map edge cases (None values, empty inputs)
- [ ] Optimize space usage when possible

### **Interview Performance** 🎯
- [ ] Solve Two Sum variants in under 3 minutes
- [ ] Explain hash table complexity clearly
- [ ] Handle follow-up questions confidently
- [ ] Code clean, bug-free solutions consistently
- [ ] Optimize solutions when prompted

### **Progress Tracking**
- [ ] **Problems Solved**: ___/15+ problems completed
- [ ] **Time Investment**: ___/20+ hours practiced
- [ ] **Mock Interviews**: ___/3 arrays&hashing focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Can solve Two Sum in under 3 minutes
- ✅ Recognize frequency counting patterns instantly  
- ✅ Choose optimal data structure (Array vs HashMap vs Set)
- ✅ Handle edge cases confidently
- ✅ Explain time/space complexity clearly

---

**Next Pattern**: [Two Pointers →](../02_two_pointers/)
