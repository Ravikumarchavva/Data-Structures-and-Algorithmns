# Backtracking 🔄

> **Interview Frequency**: 50% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #10

## 🎯 **Core Concept**
Backtracking is a systematic way to iterate through all possible configurations of a search space. It builds solutions incrementally and abandons candidates that cannot lead to a valid solution.

## 🏢 **Company Focus**
- **Google**: Complex constraint satisfaction, AI problems
- **Meta**: User preference optimization, ad targeting
- **Amazon**: Route optimization, inventory combinations
- **Apple**: Configuration management, user customization
- **Netflix**: Content recommendation combinations
- **Microsoft**: Resource allocation, scheduling

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Basic Backtracking | All FAANG |
| [Permutations](https://leetcode.com/problems/permutations/) | Medium | Array Permutation | Google, Meta |
| [Combinations](https://leetcode.com/problems/combinations/) | Medium | Choose K from N | Apple, Microsoft |
| [Subsets](https://leetcode.com/problems/subsets/) | Medium | Subset Generation | All FAANG |
| [Word Search](https://leetcode.com/problems/word-search/) | Medium | Grid Backtracking | Google, Amazon |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Constraint Checking | O(N!) | O(N²) |
| [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | Multiple Constraints | O(9^(n*n)) | O(1) |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Unlimited Use | O(N^(T/M)) | O(T/M) |
| [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | String Partitioning | O(N*2^N) | O(N) |
| [Letter Combinations Phone](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Mapping + Backtracking | O(3^N × 4^M) | O(3^N × 4^M) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Hard | Optimized Constraint Checking |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Backtracking + Trie |
| [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | Hard | Mathematical Expression Building |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Backtracking Template**
```python
def backtrack_template(candidates):
    """General backtracking template"""
    result = []
    
    def backtrack(current_solution, remaining_candidates):
        # Base case: solution is complete
        if is_solution_complete(current_solution):
            result.append(current_solution[:])  # Make a copy
            return
        
        # Try each possible next step
        for candidate in get_candidates(remaining_candidates):
            if is_valid_candidate(candidate, current_solution):
                # Make choice
                current_solution.append(candidate)
                
                # Recurse with updated state
                backtrack(current_solution, updated_candidates)
                
                # Undo choice (backtrack)
                current_solution.pop()
    
    backtrack([], candidates)
    return result

# Example: Generate Parentheses
def generate_parentheses(n):
    """Generate all valid parentheses combinations"""
    result = []
    
    def backtrack(current, open_count, close_count):
        # Base case: used all parentheses
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add opening parenthesis if we can
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add closing parenthesis if valid
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result
```

### **Pattern 2: Permutations and Combinations**
```python
def permutations(nums):
    """Generate all permutations of array"""
    result = []
    
    def backtrack(current_perm):
        # Base case: permutation is complete
        if len(current_perm) == len(nums):
            result.append(current_perm[:])
            return
        
        for num in nums:
            if num not in current_perm:  # Avoid duplicates
                current_perm.append(num)
                backtrack(current_perm)
                current_perm.pop()
    
    backtrack([])
    return result

def permutations_optimized(nums):
    """Optimized using index swapping"""
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # Swap
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            # Backtrack (swap back)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result

def combinations(n, k):
    """Choose k numbers from 1 to n"""
    result = []
    
    def backtrack(start, current_combination):
        # Base case: combination is complete
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        
        # Try each number from start to n
        for i in range(start, n + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)  # i + 1 to avoid duplicates
            current_combination.pop()
    
    backtrack(1, [])
    return result

def subsets(nums):
    """Generate all possible subsets"""
    result = []
    
    def backtrack(start, current_subset):
        # Current subset is always valid
        result.append(current_subset[:])
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    
    backtrack(0, [])
    return result
```

### **Pattern 3: Grid/Matrix Backtracking**
```python
def word_search(board, word):
    """Search for word in 2D board"""
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        # Base case: found complete word
        if index == len(word):
            return True
        
        # Check bounds and character match
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            board[row][col] != word[index] or
            board[row][col] == '#'):  # Already visited
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        found = any(backtrack(row + dr, col + dc, index + 1) 
                   for dr, dc in directions)
        
        # Backtrack (restore original value)
        board[row][col] = temp
        
        return found
    
    # Try starting from each cell
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    
    return False

def solve_sudoku(board):
    """Solve Sudoku puzzle"""
    def is_valid(board, row, col, num):
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # Try each number 1-9
                    for num in '123456789':
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            
                            if backtrack():
                                return True
                            
                            board[i][j] = '.'  # Backtrack
                    
                    return False  # No valid number found
        
        return True  # All cells filled
    
    backtrack()
    return board
```

### **Pattern 4: N-Queens Problem**
```python
def n_queens(n):
    """Solve N-Queens problem"""
    result = []
    board = ['.' * n for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check anti-diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
    
    backtrack(0)
    return result

def n_queens_optimized(n):
    """Optimized N-Queens using sets for constraint checking"""
    result = []
    
    def backtrack(row, cols, diag1, diag2, current_board):
        if row == n:
            result.append(current_board[:])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # Place queen
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current_board.append('.' * col + 'Q' + '.' * (n - col - 1))
            
            backtrack(row + 1, cols, diag1, diag2, current_board)
            
            # Remove queen (backtrack)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            current_board.pop()
    
    backtrack(0, set(), set(), set(), [])
    return result
```

### **Pattern 5: Combination Sum Variants**
```python
def combination_sum(candidates, target):
    """Numbers can be reused unlimited times"""
    result = []
    candidates.sort()  # For optimization
    
    def backtrack(start, current_combination, remaining):
        if remaining == 0:
            result.append(current_combination[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Optimization: no need to continue
            
            current_combination.append(candidates[i])
            # Use same index since we can reuse elements
            backtrack(i, current_combination, remaining - candidates[i])
            current_combination.pop()
    
    backtrack(0, [], target)
    return result

def combination_sum2(candidates, target):
    """Each number used at most once, may contain duplicates"""
    result = []
    candidates.sort()
    
    def backtrack(start, current_combination, remaining):
        if remaining == 0:
            result.append(current_combination[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            current_combination.append(candidates[i])
            # Use i + 1 since each number used at most once
            backtrack(i + 1, current_combination, remaining - candidates[i])
            current_combination.pop()
    
    backtrack(0, [], target)
    return result

def palindrome_partitioning(s):
    """Partition string into palindromic substrings"""
    result = []
    
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, current_partition):
        if start == len(s):
            result.append(current_partition[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current_partition.append(substring)
                backtrack(end, current_partition)
                current_partition.pop()
    
    backtrack(0, [])
    return result
```

## 📊 **Backtracking Complexity Analysis**

| Problem Type | Time Complexity | Space Complexity | Notes |
|--------------|----------------|------------------|-------|
| **Permutations** | O(N × N!) | O(N) | N! permutations, N to copy each |
| **Combinations** | O(C(N,K) × K) | O(K) | C(N,K) combinations |
| **Subsets** | O(N × 2^N) | O(N) | 2^N subsets |
| **N-Queens** | O(N!) | O(N) | Exponential with pruning |
| **Sudoku** | O(9^(n²)) | O(1) | Worst case, but heavy pruning |

## 🧠 **Key Insights**

### **When to Use Backtracking**
- **Generate all possibilities**: Permutations, combinations, subsets
- **Constraint satisfaction**: N-Queens, Sudoku
- **Path finding**: With specific constraints
- **Optimization**: When you need to explore all solutions

### **Backtracking vs Other Approaches**
- **vs DP**: When you need all solutions, not just optimal
- **vs Greedy**: When local choices don't guarantee global optimum
- **vs BFS/DFS**: When you need to undo choices and try alternatives

### **Optimization Techniques**
1. **Early pruning**: Check constraints before recursing
2. **Ordering**: Try most promising candidates first
3. **Constraint propagation**: Use additional data structures
4. **Memoization**: Cache results of subproblems when applicable

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Explain the approach**: "I'll use backtracking to try all possibilities"
2. **Identify constraints**: "We need to check if placing a queen here is safe"
3. **Discuss optimization**: "We can prune branches early if constraints are violated"

### **⚡ Optimization Techniques**
- **Constraint checking**: Validate before recursing
- **Early termination**: Stop when impossible to reach solution
- **State representation**: Use efficient data structures for state
- **Pruning strategies**: Skip obviously invalid branches

### **🐛 Common Pitfalls**
- **Forgetting to backtrack**: Always undo changes
- **Shallow copy issues**: Use `list[:]` or `list.copy()` for results
- **Infinite recursion**: Ensure progress toward base case
- **Inefficient constraint checking**: Use sets/maps for O(1) lookups

## 🔍 **Problem Identification**

**Use Backtracking when you see:**
- "Generate all possible..."
- "Find all combinations/permutations"
- "Place N items with constraints"
- "Partition into valid groups"
- "Solve puzzle" (Sudoku, N-Queens)
- "Path exists with conditions"

## 📈 **Template Variations**

### **Choice-Explore-Unchoice Pattern**
```python
def backtrack_pattern(state, choices):
    if is_solution(state):
        process_solution(state)
        return
    
    for choice in choices:
        if is_valid(choice, state):
            make_choice(choice, state)     # Choose
            backtrack_pattern(state, new_choices)  # Explore
            undo_choice(choice, state)     # Unchoose
```

### **Start Index Pattern** (for combinations)
```python
def combination_pattern(start_index, current_combo):
    if len(current_combo) == target_size:
        result.append(current_combo[:])
        return
    
    for i in range(start_index, len(candidates)):
        current_combo.append(candidates[i])
        combination_pattern(i + 1, current_combo)  # i+1 prevents duplicates
        current_combo.pop()
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Generate Parentheses, Letter Combinations
- Day 3-4: Permutations, Combinations
- Day 5-7: Subsets, Combination Sum

### **Week 2: Intermediate**
- Day 1-3: Word Search, Palindrome Partitioning
- Day 4-5: N-Queens, Sudoku Solver
- Day 6-7: Combination Sum variants

### **Week 3: Advanced**
- Word Search II (with Trie)
- Expression Add Operators
- Advanced constraint satisfaction problems
- Mock interview practice

## 📋 **Backtracking Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand choose-explore-unchoose pattern
- [ ] Master constraint satisfaction problems
- [ ] Know when to use backtracking vs other approaches
- [ ] Understand pruning and optimization techniques
- [ ] Master recursive decision tree exploration

### **Essential Problems** (Must Complete)
- [ ] [Subsets](https://leetcode.com/problems/subsets/) - Basic backtracking
- [ ] [Combination Sum](https://leetcode.com/problems/combination-sum/) - With duplicates allowed
- [ ] [Permutations](https://leetcode.com/problems/permutations/) - All permutations
- [ ] [Word Search](https://leetcode.com/problems/word-search/) - 2D grid backtracking
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Valid combinations
- [ ] [Letter Combinations of Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) - Multiple choices
- [ ] [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) - String partitioning

### **Intermediate Problems** (Build Proficiency)
- [ ] [Subsets II](https://leetcode.com/problems/subsets-ii/) - Handle duplicates
- [ ] [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) - No reuse
- [ ] [Permutations II](https://leetcode.com/problems/permutations-ii/) - Unique permutations
- [ ] [N-Queens](https://leetcode.com/problems/n-queens/) - Classic constraint problem
- [ ] [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) - Complex constraints
- [ ] [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) - String validation

### **Advanced Problems** (Expert Level)
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) - Multiple words + Trie
- [ ] [N-Queens II](https://leetcode.com/problems/n-queens-ii/) - Count solutions
- [ ] [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) - Mathematical constraints
- [ ] [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Minimum removals
- [ ] [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) - Path constraints

### **Pattern Recognition** 🧠
- [ ] Identify when all solutions needed (vs first solution)
- [ ] Recognize constraint satisfaction problems
- [ ] Spot when pruning can optimize performance
- [ ] Know when backtracking beats dynamic programming
- [ ] Understand decision tree structure

### **Implementation Skills** 💻
- [ ] Master the recursive backtracking template
- [ ] Handle duplicate elimination correctly
- [ ] Implement efficient constraint checking
- [ ] Use proper data structure for state tracking
- [ ] Apply pruning techniques effectively

### **Interview Performance** 🎯
- [ ] Solve Subsets in under 5 minutes
- [ ] Implement backtracking template from memory
- [ ] Handle duplicate cases correctly
- [ ] Explain time complexity (often exponential)
- [ ] Optimize with early pruning when possible

### **Progress Tracking**
- [ ] **Problems Solved**: ___/16+ problems completed
- [ ] **Time Investment**: ___/20+ hours practiced
- [ ] **Mock Interviews**: ___/2 backtracking focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Master the choose-explore-unchoose pattern
- ✅ Implement efficient constraint checking
- ✅ Handle duplicates correctly in combinations
- ✅ Optimize with early pruning
- ✅ Solve N-Queens and Sudoku confidently

---

**Previous**: [← Heap/Priority Queue](../09_heap_priority_queue/) | **Next**: [Graphs →](../11_graphs/)
