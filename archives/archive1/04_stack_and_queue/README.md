# Stack & Queue 📚🔄

> **Interview Frequency**: 70% | **Difficulty**: ⭐⭐ | **Pattern Priority**: #4

## 🎯 **Core Concept**
Stacks (LIFO) and Queues (FIFO) are fundamental for managing sequential data, parsing expressions, and implementing other data structures efficiently.

## 🏢 **Company Focus**
- **Google**: Expression parsing, monotonic stacks
- **Meta**: Browser history, undo operations
- **Amazon**: Order processing, inventory systems
- **Apple**: UI navigation stacks
- **Microsoft**: Compiler design, parsing

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Basic Stack | All FAANG |
| [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Stack Design | Google, Amazon |
| [Evaluate RPN](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Expression Evaluation | Microsoft |
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Stack + Backtracking | Google, Meta |
| [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | Data Structure Design | Apple |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic Stack | O(n) | O(n) |
| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Stack for Heights | O(n) | O(n) |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic Deque | O(n) | O(k) |
| [Next Greater Element](https://leetcode.com/problems/next-greater-element-i/) | Easy | Monotonic Stack | O(n) | O(n) |
| [Decode String](https://leetcode.com/problems/decode-string/) | Medium | Nested Stack Processing | O(n) | O(n) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | Expression Parsing with Operators |
| [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | Stack + Dynamic Programming |
| [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Medium | Greedy + Monotonic Stack |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Stack Operations**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Example: Valid Parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    return not stack  # Should be empty
```

### **Pattern 2: Monotonic Stack**
```python
def daily_temperatures(temperatures):
    """Find next warmer temperature for each day"""
    result = [0] * len(temperatures)
    stack = []  # Store indices
    
    for i, temp in enumerate(temperatures):
        # While stack not empty and current temp > temp at stack top
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        
        stack.append(i)
    
    return result

def next_greater_element(nums):
    """Find next greater element for each number"""
    result = [-1] * len(nums)
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    
    return result
```

### **Pattern 3: Queue Implementation**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop() if self.stack2 else None
```

### **Pattern 4: Expression Evaluation**
```python
def evaluate_rpn(tokens):
    """Evaluate Reverse Polish Notation"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                result = int(a / b)  # Truncate towards zero
            
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]

def decode_string(s):
    """Decode string like '3[a2[c]]' -> 'accaccacc'"""
    stack = []
    current_num = 0
    current_string = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop and apply repetition
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char
    
    return current_string
```

## 📊 **Data Structure Comparison**

| Operation | Stack | Queue | Deque |
|-----------|-------|-------|-------|
| **Insert** | push() - O(1) | enqueue() - O(1) | append/appendleft() - O(1) |
| **Remove** | pop() - O(1) | dequeue() - O(1) | pop/popleft() - O(1) |
| **Access** | peek() - O(1) | front() - O(1) | peek both ends - O(1) |
| **Search** | O(n) | O(n) | O(n) |
| **Space** | O(n) | O(n) | O(n) |

## 🧠 **Key Insights**

### **When to Use Stack**
- **Parentheses/Bracket matching**: Natural LIFO behavior
- **Expression evaluation**: RPN, infix to postfix
- **Undo operations**: Most recent action first
- **Function call management**: Call stack
- **Depth-first traversal**: DFS implementation

### **When to Use Queue**
- **Breadth-first traversal**: BFS implementation
- **Process scheduling**: First come, first served
- **Buffer for streaming data**: Producer-consumer
- **Level-order tree traversal**: Process by levels

### **Monotonic Stack Applications**
- **Next/Previous greater element**: Temperature, stock prices
- **Histogram problems**: Largest rectangle
- **Sliding window extrema**: Combined with deque

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify requirements**: "Should I handle invalid input?"
2. **Explain choice**: "Stack is perfect for LIFO behavior in parentheses"
3. **Mention alternatives**: "Could use recursion, but stack is more explicit"

### **⚡ Optimization Techniques**
- **Use deque**: More efficient than list for queue operations
- **Monotonic stacks**: Achieve O(n) for next greater element problems
- **Space optimization**: Reuse containers when possible

### **🐛 Common Pitfalls**
- **Empty stack/queue operations**: Always check before pop/dequeue
- **Stack overflow**: Very deep recursion can cause issues
- **Memory leaks**: Clear references when removing elements
- **Queue using arrays**: Inefficient without circular buffer

## 🔍 **Problem Identification**

**Use Stack when you see:**
- "Valid parentheses/brackets"
- "Evaluate expression"
- "Next greater/smaller element"
- "Undo operations"
- "Nested structures"

**Use Queue when you see:**
- "First in, first out"
- "Level-order traversal"
- "Breadth-first search"
- "Process scheduling"
- "Sliding window maximum"

## 📈 **Complexity Patterns**

| Pattern | Time Complexity | Space Complexity | Use Case |
|---------|----------------|------------------|----------|
| **Basic Stack/Queue** | O(1) per operation | O(n) storage | Standard operations |
| **Monotonic Stack** | O(n) total | O(n) worst case | Next greater element |
| **Expression Parsing** | O(n) | O(n) | Calculator, decoder |
| **Design Problems** | O(1) amortized | O(n) | Min stack, queue with stacks |

## 🎭 **Advanced Patterns**

### **Min Stack with O(1) Operations**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        # Push current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
```

### **Sliding Window Maximum using Deque**
```python
from collections import deque

def sliding_window_maximum(nums, k):
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (won't be max)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Valid Parentheses, Implement Stack/Queue
- Day 3-4: Min Stack, Queue using Stacks
- Day 5-7: Evaluate RPN, Next Greater Element

### **Week 2: Intermediate**
- Day 1-3: Daily Temperatures, Decode String
- Day 4-5: Generate Parentheses
- Day 6-7: Sliding Window Maximum

### **Week 3: Advanced**
- Largest Rectangle in Histogram
- Basic Calculator
- Mock interview practice

## 📋 **Stack & Queue Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand LIFO (Stack) vs FIFO (Queue) operations
- [ ] Master monotonic stack/queue patterns
- [ ] Know when stack optimizes recursion
- [ ] Understand parentheses/bracket matching
- [ ] Master expression evaluation techniques

### **Essential Problems** (Must Complete)
- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Basic stack usage
- [ ] [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) - Data structure design
- [ ] [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) - Reverse design
- [ ] [Min Stack](https://leetcode.com/problems/min-stack/) - Stack with additional operations
- [ ] [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Expression evaluation
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Backtracking with stack
- [ ] [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) - Monotonic stack

### **Intermediate Problems** (Build Proficiency)
- [ ] [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) - Monotonic stack pattern
- [ ] [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) - Circular array
- [ ] [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) - Collision simulation
- [ ] [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) - Greedy stack
- [ ] [Decode String](https://leetcode.com/problems/decode-string/) - Nested parsing
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Monotonic deque

### **Advanced Problems** (Expert Level)
- [ ] [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Complex monotonic stack
- [ ] [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) - 2D histogram
- [ ] [Basic Calculator](https://leetcode.com/problems/basic-calculator/) - Expression parsing
- [ ] [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) - Operator precedence
- [ ] [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) - Greedy stack optimization

### **Pattern Recognition** 🧠
- [ ] Identify when parentheses/brackets need validation
- [ ] Recognize monotonic stack opportunities
- [ ] Spot expression parsing requirements
- [ ] Know when recursion can be optimized with stack
- [ ] Understand when queue ensures order processing

### **Implementation Skills** 💻
- [ ] Implement stack and queue from scratch
- [ ] Handle edge cases (empty structures, overflow)
- [ ] Optimize space usage when possible
- [ ] Use deque for sliding window maximum
- [ ] Code clean bracket matching logic

### **Interview Performance** 🎯
- [ ] Solve Valid Parentheses in under 3 minutes
- [ ] Explain LIFO vs FIFO clearly
- [ ] Design custom stack/queue with constraints
- [ ] Handle follow-up questions about space optimization
- [ ] Debug stack overflow/underflow issues

### **Progress Tracking**
- [ ] **Problems Solved**: ___/17+ problems completed
- [ ] **Time Investment**: ___/20+ hours practiced
- [ ] **Mock Interviews**: ___/2 stack&queue focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Implement stack and queue from scratch
- ✅ Recognize when to use monotonic stack
- ✅ Handle edge cases (empty structures)
- ✅ Optimize expression evaluation problems
- ✅ Explain LIFO vs FIFO clearly

---

**Previous**: [← Sliding Window](../03_sliding_window/) | **Next**: [Binary Search →](../05_binary_search/)
