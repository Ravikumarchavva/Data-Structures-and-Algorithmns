# Dynamic Programming 🔄💡

> **Interview Frequency**: 60% | **Difficulty**: ⭐⭐⭐⭐ | **Pattern Priority**: #13

## 🎯 **Core Concept**
Dynamic Programming solves optimization problems by breaking them into overlapping subproblems and storing solutions to avoid recomputation. Master memoization and tabulation approaches.

## 🏢 **Company Focus**
- **Google**: Complex DP with multiple dimensions, optimization
- **Meta**: User engagement optimization, recommendation algorithms
- **Amazon**: Resource allocation, delivery optimization
- **Apple**: Performance optimization algorithms
- **Microsoft**: Game theory, scheduling optimization

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Basic DP | All FAANG |
| [House Robber](https://leetcode.com/problems/house-robber/) | Medium | Linear DP | Amazon, Apple |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Unbounded Knapsack | Google, Meta |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Subsequence DP | All FAANG |
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | Grid DP | Google, Amazon |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D DP | O(m*n) | O(m*n) |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | Hard | String DP | O(m*n) | O(m*n) |
| [0/1 Knapsack](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) | Medium | Classic DP | O(n*W) | O(n*W) |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | String DP | O(n²) | O(n²) |
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | State Tracking | O(n) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Best Time to Buy Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | State Machine DP |
| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | Interval DP |
| [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) | Hard | 3D DP Path Problems |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Linear DP (1D)**
```python
def climbing_stairs(n):
    """Basic linear DP - number of ways to reach step n"""
    if n <= 1:
        return 1
    
    # Bottom-up approach
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def house_robber(nums):
    """Cannot rob adjacent houses"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Space optimized
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1
```

### **Pattern 2: Grid DP (2D Path Problems)**
```python
def unique_paths(m, n):
    """Number of paths from top-left to bottom-right"""
    # Space optimized to O(n)
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]

def min_path_sum(grid):
    """Minimum sum path from top-left to bottom-right"""
    m, n = len(grid), len(grid[0])
    
    # Modify input array (or create new dp array)
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[m-1][n-1]
```

### **Pattern 3: String DP**
```python
def longest_common_subsequence(text1, text2):
    """LCS - classic 2D DP"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def edit_distance(word1, word2):
    """Minimum operations to convert word1 to word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]
```

### **Pattern 4: Knapsack DP**
```python
def coin_change(coins, amount):
    """Minimum coins to make amount (Unbounded Knapsack)"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def knapsack_01(weights, values, capacity):
    """0/1 Knapsack - each item can be used once"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take item
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Take item
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### **Pattern 5: Subsequence DP**
```python
def longest_increasing_subsequence(nums):
    """Length of LIS"""
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lis_optimized(nums):
    """LIS with O(n log n) using binary search"""
    from bisect import bisect_left
    
    tails = []
    
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)
```

## 📊 **DP Pattern Classification**

| Pattern | Examples | Recurrence Type | Optimization |
|---------|----------|----------------|--------------|
| **Linear DP** | Fibonacci, House Robber | dp[i] = f(dp[i-1], dp[i-2]) | Space: O(n) → O(1) |
| **Grid DP** | Unique Paths, Min Path Sum | dp[i][j] = f(dp[i-1][j], dp[i][j-1]) | Space: O(m*n) → O(n) |
| **String DP** | LCS, Edit Distance | dp[i][j] = f(s1[i], s2[j]) | Often 2D |
| **Knapsack DP** | Coin Change, 0/1 Knapsack | Include/Exclude decisions | Space optimization possible |
| **Interval DP** | Palindrome, Matrix Chain | dp[i][j] = optimal for range [i,j] | Usually O(n³) |

## 🧠 **Key Insights**

### **DP Problem Identification**
1. **Optimal Substructure**: Optimal solution contains optimal subsolutions
2. **Overlapping Subproblems**: Same subproblems solved multiple times
3. **Decision at each step**: Choose between options
4. **Optimization goal**: Minimize/maximize some value

### **Top-Down vs Bottom-Up**
- **Memoization (Top-Down)**: Recursive + cache, easier to think
- **Tabulation (Bottom-Up)**: Iterative, often more space efficient

### **State Design Strategy**
- **What information do I need**: To make optimal decision at each step
- **State transition**: How current state relates to previous states
- **Base cases**: Simple cases where answer is known

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify DP**: "This has optimal substructure and overlapping subproblems"
2. **Define state**: "dp[i] represents the optimal solution for first i elements"
3. **Explain transition**: "For each element, we can either include it or exclude it"

### **⚡ Optimization Techniques**
- **Space optimization**: Reduce dimensions when only previous values needed
- **Memoization**: Add caching to recursive solution
- **State compression**: Use bit manipulation for subset problems

### **🐛 Common Pitfalls**
- **Wrong state definition**: Not capturing enough information
- **Incorrect base cases**: Edge cases not handled properly
- **Index errors**: Off-by-one in array access
- **Infinite recursion**: No proper base case in memoization

## 🔍 **Problem Identification**

**Use DP when you see:**
- "Find optimal solution" (min/max)
- "Count number of ways"
- "Is it possible to..." 
- Problems with choices at each step
- Recursive solution with overlapping subproblems

## 📈 **Complexity Patterns**

| DP Type | Time Complexity | Space Complexity | Space Optimized |
|---------|----------------|------------------|-----------------|
| **1D Linear** | O(n) | O(n) | O(1) |
| **2D Grid** | O(m*n) | O(m*n) | O(min(m,n)) |
| **String (2D)** | O(m*n) | O(m*n) | O(min(m,n)) |
| **Knapsack** | O(n*W) | O(n*W) | O(W) |
| **Interval** | O(n³) | O(n²) | Usually not optimizable |

## 🎯 **DP Development Process**

### **Step-by-Step Approach**
1. **Recognize DP**: Optimal substructure + overlapping subproblems
2. **Define state**: What does dp[i] represent?
3. **State transition**: How to compute dp[i] from previous states?
4. **Base cases**: What are the simplest cases?
5. **Implementation**: Top-down (recursion + memo) or bottom-up (tabulation)
6. **Optimization**: Can we reduce space complexity?

### **Common State Definitions**
- **dp[i]**: Optimal solution for first i elements
- **dp[i][j]**: Optimal solution for subproblem ending at (i,j)
- **dp[i][j][k]**: 3D problems with additional constraint k

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Climbing Stairs, Fibonacci variations
- Day 3-4: House Robber, Min Cost Climbing Stairs
- Day 5-7: Unique Paths, Min Path Sum

### **Week 2: Intermediate**
- Day 1-3: Coin Change, LIS, LCS
- Day 4-5: Edit Distance, Palindromic Substrings
- Day 6-7: 0/1 Knapsack variations

### **Week 3-4: Advanced**
- Maximum Product Subarray
- Best Time to Buy/Sell Stock series
- Burst Balloons, Cherry Pickup
- Mock interview practice

## 📋 **Dynamic Programming Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand optimal substructure property
- [ ] Master overlapping subproblems identification
- [ ] Know memoization vs tabulation approaches
- [ ] Understand state definition and transitions
- [ ] Master space optimization techniques

### **Essential Problems** (Must Complete)
- [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Basic DP introduction
- [ ] [House Robber](https://leetcode.com/problems/house-robber/) - Linear DP
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/) - Unbounded knapsack
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - LIS pattern
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - 2D DP
- [ ] [0-1 Knapsack](https://leetcode.com/problems/partition-equal-subset-sum/) - Classic knapsack
- [ ] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Kadane's algorithm

### **Intermediate Problems** (Build Proficiency)
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) - Circular array
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) - String DP
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/) - 2D grid DP
- [ ] [Jump Game](https://leetcode.com/problems/jump-game/) - Greedy vs DP
- [ ] [Word Break](https://leetcode.com/problems/word-break/) - String partitioning
- [ ] [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - Ordering matters
- [ ] [Target Sum](https://leetcode.com/problems/target-sum/) - Subset sum variant

### **Advanced Problems** (Expert Level)
- [ ] [Edit Distance](https://leetcode.com/problems/edit-distance/) - Classic 2D DP
- [ ] [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) - Complex pattern matching
- [ ] [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) - State machine DP
- [ ] [Burst Balloons](https://leetcode.com/problems/burst-balloons/) - Interval DP
- [ ] [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) - Complex optimization

### **Pattern Recognition** 🧠
- [ ] Identify optimization problems with choices
- [ ] Recognize overlapping subproblems
- [ ] Spot when greedy doesn't work but DP does
- [ ] Know classic DP patterns (knapsack, LIS, LCS)
- [ ] Understand when to use 1D vs 2D DP

### **Implementation Skills** 💻
- [ ] Master both top-down and bottom-up approaches
- [ ] Optimize space complexity (2D → 1D)
- [ ] Handle base cases and edge conditions
- [ ] Debug state transition logic
- [ ] Implement memoization correctly

### **Interview Performance** 🎯
- [ ] Identify DP problems quickly
- [ ] Define DP state clearly
- [ ] Implement memoization solution first
- [ ] Optimize to tabulation when needed
- [ ] Explain time/space complexity correctly

### **Progress Tracking**
- [ ] **Problems Solved**: ___/20+ problems completed
- [ ] **Time Investment**: ___/30+ hours practiced
- [ ] **Mock Interviews**: ___/4 DP focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Identify DP problems in under 2 minutes
- ✅ Define state and transitions correctly
- ✅ Implement both memoization and tabulation
- ✅ Optimize space complexity when possible
- ✅ Handle edge cases and base cases properly

---

**Previous**: [← Advanced Graphs](../12_advanced_graphs/) | **Next**: [Greedy →](../14_greedy/)
