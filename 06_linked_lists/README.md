# Linked Lists 🔗

> **Interview Frequency**: 60% | **Difficulty**: ⭐⭐ | **Pattern Priority**: #6

## 🎯 **Core Concept**
Linked Lists are linear data structures where elements are stored in nodes, each pointing to the next. Master pointer manipulation, cycle detection, and list merging.

## 🏢 **Company Focus**
- **Google**: Complex linked list algorithms, memory management
- **Meta**: Social connection graphs, feed algorithms
- **Amazon**: Order processing chains, inventory linked systems
- **Apple**: Device connection protocols, data streaming
- **Microsoft**: File system links, process scheduling

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Basic Pointer Manipulation | All FAANG |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Two Pointer Merge | Entry Level |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd's Algorithm | All FAANG |
| [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Two Pointers | Google, Amazon |
| [Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Fast & Slow Pointers | Apple, Microsoft |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Digit-by-digit addition | O(max(m,n)) | O(max(m,n)) |
| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Easy | Two pointer technique | O(m+n) | O(1) |
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | Reverse + Compare | O(n) | O(1) |
| [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | Single pass removal | O(n) | O(1) |
| [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | Medium | Pointer manipulation | O(n) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Divide & Conquer + Heap |
| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Deep copying with random pointers |
| [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Doubly Linked List + Hash Map |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Node Operations**
```python
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """Reverse linked list iteratively"""
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

def reverse_list_recursive(head):
    """Reverse linked list recursively"""
    if not head or not head.next:
        return head
    
    reversed_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return reversed_head
```

### **Pattern 2: Two Pointers (Fast & Slow)**
```python
def has_cycle(head):
    """Floyd's Cycle Detection Algorithm"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def find_middle(head):
    """Find middle node using slow/fast pointers"""
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def remove_nth_from_end(head, n):
    """Remove nth node from end using two pointers"""
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    
    return dummy.next
```

### **Pattern 3: Merge Operations**
```python
def merge_two_lists(list1, list2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = list1 or list2
    
    return dummy.next

def merge_k_lists(lists):
    """Merge k sorted lists using divide and conquer"""
    if not lists:
        return None
    
    def merge_two(l1, l2):
        return merge_two_lists(l1, l2)
    
    while len(lists) > 1:
        merged_lists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two(l1, l2))
        
        lists = merged_lists
    
    return lists[0]
```

### **Pattern 4: List Manipulation**
```python
def add_two_numbers(l1, l2):
    """Add two numbers represented as linked lists"""
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

def swap_pairs(head):
    """Swap every two adjacent nodes"""
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        # Nodes to be swapped
        first = prev.next
        second = prev.next.next
        
        # Swap
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move prev pointer
        prev = first
    
    return dummy.next
```

### **Pattern 5: Advanced Pointer Manipulation**
```python
def copy_random_list(head):
    """Copy list with random pointers"""
    if not head:
        return None
    
    # Step 1: Create new nodes and interweave with original
    current = head
    while current:
        new_node = ListNode(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Step 2: Set random pointers for new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the lists
    dummy = ListNode(0)
    new_current = dummy
    current = head
    
    while current:
        new_current.next = current.next
        current.next = current.next.next
        new_current = new_current.next
        current = current.next
    
    return dummy.next

def is_palindrome(head):
    """Check if linked list is palindrome"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second_half = reverse_list(slow)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True
```

## 📊 **Linked List vs Array Comparison**

| Operation | Linked List | Array |
|-----------|-------------|-------|
| **Access** | O(n) | O(1) |
| **Search** | O(n) | O(n) |
| **Insert (beginning)** | O(1) | O(n) |
| **Insert (end)** | O(n) or O(1) with tail | O(1) amortized |
| **Delete** | O(1) with reference | O(n) |
| **Memory** | Extra space for pointers | Contiguous block |

## 🧠 **Key Insights**

### **When to Use Linked Lists**
- **Frequent insertions/deletions**: Especially at beginning
- **Unknown size**: Dynamic size requirements
- **Memory constraints**: When arrays would be too large

### **Common Linked List Patterns**
- **Dummy node**: Simplifies edge cases
- **Two pointers**: Fast/slow for cycle detection, middle finding
- **Reverse technique**: Useful for palindrome checks
- **Merge pattern**: Combine multiple sorted lists

### **Memory Management**
- **Node allocation**: Each node requires separate memory allocation
- **Cache locality**: Poor compared to arrays
- **Pointer overhead**: Extra memory for storing addresses

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Draw the list**: Visualize pointer movements
2. **Explain edge cases**: "What if the list is empty or has one node?"
3. **Discuss space complexity**: "Using dummy node for cleaner code"

### **⚡ Optimization Techniques**
- **Dummy head**: Simplifies insertion/deletion at head
- **Two pointers**: Solve in single pass where possible
- **In-place operations**: Avoid extra space when possible

### **🐛 Common Pitfalls**
- **Null pointer errors**: Always check node.next before accessing
- **Memory leaks**: In languages requiring manual memory management
- **Infinite loops**: Ensure progress in while loops
- **Losing references**: Keep track of nodes before modifying pointers

## 🔍 **Problem Identification**

**Use Linked List algorithms when you see:**
- "Linked list" in problem statement
- "Reverse a list"
- "Detect cycle"
- "Merge sorted lists"
- "Remove nodes"
- "Find middle/nth from end"

## 📈 **Complexity Analysis**

| Pattern | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| **Traversal** | O(n) | O(1) | Single pass through list |
| **Reverse** | O(n) | O(1) iterative, O(n) recursive | In-place reversal |
| **Merge Two Lists** | O(m + n) | O(1) | Linear merge |
| **Cycle Detection** | O(n) | O(1) | Floyd's algorithm |
| **Find Middle** | O(n) | O(1) | Fast/slow pointers |

## 🎯 **Advanced Data Structures**

### **Doubly Linked List**
```python
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """LRU Cache using Doubly Linked List + HashMap"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head and tail
        self.head = DoublyListNode()
        self.tail = DoublyListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move node to head (mark as recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove last node"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key):
        node = self.cache.get(key)
        
        if node:
            self._move_to_head(node)
            return node.val
        
        return -1
    
    def put(self, key, value):
        node = self.cache.get(key)
        
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            new_node = DoublyListNode(value)
            
            if len(self.cache) >= self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            self.cache[key] = new_node
            new_node.key = key
            self._add_node(new_node)
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Reverse Linked List, Merge Two Sorted Lists
- Day 3-4: Linked List Cycle, Middle of Linked List
- Day 5-7: Remove Nth Node, Add Two Numbers

### **Week 2: Intermediate**
- Day 1-3: Palindrome Linked List, Intersection of Lists
- Day 4-5: Swap Nodes in Pairs, Remove Duplicates
- Day 6-7: Copy List with Random Pointer

### **Week 3: Advanced**
- Merge K Sorted Lists
- LRU Cache implementation
- Advanced pointer manipulation problems
- Mock interview practice

## 📋 **Linked Lists Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand pointer manipulation and node creation
- [ ] Master dummy node technique for edge cases
- [ ] Know Floyd's cycle detection algorithm
- [ ] Understand fast/slow pointer patterns
- [ ] Master list reversal techniques

### **Essential Problems** (Must Complete)
- [ ] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - Basic reversal
- [ ] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Merging technique
- [ ] [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) - Cycle detection
- [ ] [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Two pointer
- [ ] [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) - Fast/slow pointers
- [ ] [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) - Reversal + comparison
- [ ] [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) - Basic removal

### **Intermediate Problems** (Build Proficiency)
- [ ] [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Mathematical operations
- [ ] [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) - Two list traversal
- [ ] [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - Group reversal
- [ ] [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) - Pair manipulation
- [ ] [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) - Complex removal
- [ ] [Rotate List](https://leetcode.com/problems/rotate-list/) - List rotation
- [ ] [Partition List](https://leetcode.com/problems/partition-list/) - List partitioning

### **Advanced Problems** (Expert Level)
- [ ] [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - Complex merging
- [ ] [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - Deep copying
- [ ] [LRU Cache](https://leetcode.com/problems/lru-cache/) - Cache implementation
- [ ] [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) - Complex structure
- [ ] [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) - Partial reversal

### **Pattern Recognition** 🧠
- [ ] Identify when dummy nodes simplify logic
- [ ] Recognize cycle detection opportunities
- [ ] Spot fast/slow pointer applications
- [ ] Know when to use in-place vs extra space
- [ ] Understand reversal as preprocessing step

### **Implementation Skills** 💻
- [ ] Handle null pointer edge cases correctly
- [ ] Implement clean pointer manipulation
- [ ] Use dummy nodes to avoid special cases
- [ ] Master both iterative and recursive approaches
- [ ] Debug pointer assignment errors quickly

### **Interview Performance** 🎯
- [ ] Solve Reverse Linked List in under 3 minutes
- [ ] Implement cycle detection from memory
- [ ] Handle edge cases without prompting
- [ ] Explain space vs time complexity trade-offs
- [ ] Debug pointer errors efficiently

### **Progress Tracking**
- [ ] **Problems Solved**: ___/18+ problems completed
- [ ] **Time Investment**: ___/22+ hours practiced
- [ ] **Mock Interviews**: ___/3 linked list focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Master pointer manipulation without errors
- ✅ Implement Floyd's cycle detection algorithm
- ✅ Handle edge cases (empty list, single node)
- ✅ Use dummy nodes effectively
- ✅ Optimize space complexity using two-pointer techniques

---

**Previous**: [← Binary Search](../05_binary_search/) | **Next**: [Trees →](../07_trees/)
