# Trees 🌳

> **Interview Frequency**: 85% | **Difficulty**: ⭐⭐⭐ | **Pattern Priority**: #7

## 🎯 **Core Concept**
Trees are hierarchical data structures fundamental to many algorithms. Master traversals, binary search trees, and tree manipulation techniques.

## 🏢 **Company Focus**
- **Google**: Complex tree algorithms, balanced trees
- **Meta**: Hierarchical data modeling, decision trees
- **Amazon**: File systems, organizational hierarchies
- **Apple**: UI component trees, file organization
- **Microsoft**: Parse trees, expression trees

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | Tree Traversal | All FAANG |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Tree Recursion | Entry Level |
| [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | Tree Comparison | Apple, Microsoft |
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Tree Manipulation | Google, Meta |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS on Trees | All FAANG |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | BST Property | O(n) | O(h) |
| [Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Tree Navigation | O(n) | O(h) |
| [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Tree Metrics | O(n) | O(h) |
| [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Tree Encoding | O(n) | O(n) |
| [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | Level Order | O(n) | O(h) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Tree DP |
| [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Tree Construction |
| [Vertical Order Traversal](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Hard | Coordinate-based Traversal |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Tree Traversals**
```python
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_recursive(root):
    """Left -> Root -> Right"""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def inorder_iterative(root):
    """Iterative inorder using stack"""
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

def level_order_traversal(root):
    """BFS - Level by level"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### **Pattern 2: Tree Recursion (Divide & Conquer)**
```python
def max_depth(root):
    """Maximum depth of binary tree"""
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)

def is_same_tree(p, q):
    """Check if two trees are identical"""
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

def invert_tree(root):
    """Invert binary tree (mirror)"""
    if not root:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root
```

### **Pattern 3: Binary Search Tree Operations**
```python
def is_valid_bst(root):
    """Validate BST property"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def search_bst(root, val):
    """Search in BST"""
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)

def insert_into_bst(root, val):
    """Insert into BST"""
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root
```

### **Pattern 4: Tree Path Problems**
```python
def has_path_sum(root, target_sum):
    """Check if path exists with given sum"""
    if not root:
        return False
    
    if not root.left and not root.right:  # Leaf node
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))

def path_sum_all_paths(root, target_sum):
    """Find all root-to-leaf paths with target sum"""
    result = []
    
    def dfs(node, current_path, remaining):
        if not node:
            return
        
        current_path.append(node.val)
        
        if not node.left and not node.right and remaining == node.val:
            result.append(current_path[:])  # Copy path
        else:
            dfs(node.left, current_path, remaining - node.val)
            dfs(node.right, current_path, remaining - node.val)
        
        current_path.pop()  # Backtrack
    
    dfs(root, [], target_sum)
    return result

def max_path_sum(root):
    """Maximum path sum in binary tree"""
    max_sum = float('-inf')
    
    def max_path_helper(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Get max sum from left and right subtrees
        left_sum = max(0, max_path_helper(node.left))
        right_sum = max(0, max_path_helper(node.right))
        
        # Current path sum through this node
        current_max = node.val + left_sum + right_sum
        max_sum = max(max_sum, current_max)
        
        # Return max sum path starting from this node
        return node.val + max(left_sum, right_sum)
    
    max_path_helper(root)
    return max_sum
```

### **Pattern 5: Lowest Common Ancestor**
```python
def lowest_common_ancestor(root, p, q):
    """LCA in binary tree"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root  # Found both nodes in different subtrees
    
    return left or right  # Return non-null result

def lca_bst(root, p, q):
    """LCA in BST (more efficient)"""
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)
    else:
        return root  # Split point found
```

## 📊 **Tree Types & Properties**

| Tree Type | Properties | Use Cases | Time Complexity |
|-----------|------------|-----------|-----------------|
| **Binary Tree** | Each node has ≤ 2 children | General hierarchical data | O(n) traversal |
| **Binary Search Tree** | Left < Root < Right | Sorted data, searching | O(log n) search (balanced) |
| **Complete Binary Tree** | All levels filled except last | Heaps, array representation | O(log n) height |
| **Perfect Binary Tree** | All levels completely filled | Theoretical analysis | Height = log n |
| **Balanced Tree** | Height difference ≤ 1 | Performance guarantees | O(log n) operations |

## 🧠 **Key Insights**

### **Tree Traversal Applications**
- **Inorder (BST)**: Gets elements in sorted order
- **Preorder**: Tree copying, prefix expressions
- **Postorder**: Tree deletion, postfix expressions
- **Level Order**: BFS, printing by levels

### **Recursive Thinking Pattern**
1. **Base case**: What happens at null/leaf nodes?
2. **Recursive case**: How do children contribute to solution?
3. **Combine results**: How to merge left and right subtree results?

### **Tree vs Graph Key Differences**
- **Trees**: No cycles, n-1 edges for n nodes, connected
- **Graphs**: Can have cycles, arbitrary edge count

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Clarify tree type**: "Is this a BST or general binary tree?"
2. **Explain traversal choice**: "Inorder gives sorted sequence for BST"
3. **Discuss recursion**: "Base case is null node, recursive case processes children"

### **⚡ Optimization Techniques**
- **Iterative traversals**: Use stack/queue to avoid recursion overhead
- **Morris traversal**: O(1) space for inorder/preorder
- **Early termination**: Stop when answer is found

### **🐛 Common Pitfalls**
- **Null pointer errors**: Always check if node exists before accessing
- **Incorrect base cases**: Handle empty tree and single node cases
- **Stack overflow**: Very deep trees can cause recursion issues
- **BST property violation**: Not maintaining left < root < right

## 🔍 **Problem Identification**

**Use Tree algorithms when you see:**
- "Binary tree" or "BST" in problem statement
- "Root-to-leaf paths"
- "Tree traversal" or "visit nodes"
- "Lowest common ancestor"
- "Tree depth/height"
- Hierarchical data structures

## 📈 **Complexity Analysis**

| Operation | Binary Tree | BST (Balanced) | BST (Skewed) |
|-----------|-------------|----------------|--------------|
| **Search** | O(n) | O(log n) | O(n) |
| **Insert** | O(log n) avg | O(log n) | O(n) |
| **Delete** | O(log n) avg | O(log n) | O(n) |
| **Traversal** | O(n) | O(n) | O(n) |
| **Space (Recursion)** | O(h) | O(log n) | O(n) |

## 🎯 **Tree Construction Problems**
```python
def build_tree_preorder_inorder(preorder, inorder):
    """Construct tree from preorder and inorder traversal"""
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = build_tree_preorder_inorder(
        preorder[1:mid+1], 
        inorder[:mid]
    )
    root.right = build_tree_preorder_inorder(
        preorder[mid+1:], 
        inorder[mid+1:]
    )
    
    return root

def serialize_tree(root):
    """Serialize tree to string"""
    def serialize_helper(node):
        if not node:
            return "null"
        
        return f"{node.val},{serialize_helper(node.left)},{serialize_helper(node.right)}"
    
    return serialize_helper(root)

def deserialize_tree(data):
    """Deserialize string to tree"""
    def deserialize_helper():
        val = next(vals)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = deserialize_helper()
        node.right = deserialize_helper()
        return node
    
    vals = iter(data.split(','))
    return deserialize_helper()
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Tree traversals (recursive & iterative)
- Day 3-4: Maximum depth, same tree, invert tree
- Day 5-7: Level order traversal, binary tree paths

### **Week 2: Intermediate**
- Day 1-3: Validate BST, LCA, diameter
- Day 4-5: Path sum problems, right side view
- Day 6-7: Tree construction from traversals

### **Week 3: Advanced**
- Serialize/Deserialize tree
- Maximum path sum
- Vertical order traversal
- Mock interview practice

## 📋 **Trees Mastery Checklist**

### **Core Concepts** ✅
- [ ] Understand tree structure and terminology
- [ ] Master recursive tree traversal patterns
- [ ] Know BST properties and optimizations
- [ ] Understand tree construction techniques
- [ ] Master iterative traversal using stacks

### **Essential Problems** (Must Complete)
- [ ] [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Basic tree manipulation
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Depth calculation
- [ ] [Same Tree](https://leetcode.com/problems/same-tree/) - Tree comparison
- [ ] [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - Subtree matching
- [ ] [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - BST properties
- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - BFS traversal
- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - BST validation

### **Intermediate Problems** (Build Proficiency)
- [ ] [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) - Tree construction
- [ ] [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) - BST properties
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - Level traversal variant
- [ ] [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) - Path tracking
- [ ] [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) - Path calculations
- [ ] [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Height checking
- [ ] [Path Sum](https://leetcode.com/problems/path-sum/) - Path validation

### **Advanced Problems** (Expert Level)
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) - Complex path calculations
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) - Tree serialization
- [ ] [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) - Complex traversal
- [ ] [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) - BST repair
- [ ] [House Robber III](https://leetcode.com/problems/house-robber-iii/) - Tree DP

### **Pattern Recognition** 🧠
- [ ] Identify when recursion simplifies tree problems
- [ ] Recognize BST optimization opportunities
- [ ] Spot level-order traversal requirements
- [ ] Know when to use iterative vs recursive approaches
- [ ] Understand tree DP patterns

### **Implementation Skills** 💻
- [ ] Implement all traversal methods (in/pre/post-order)
- [ ] Handle null nodes correctly in recursion
- [ ] Use helper functions for complex tree operations
- [ ] Implement both recursive and iterative solutions
- [ ] Master tree construction from traversals

### **Interview Performance** 🎯
- [ ] Solve Invert Binary Tree in under 2 minutes
- [ ] Implement tree traversals from memory
- [ ] Handle edge cases (null root, single node)
- [ ] Explain recursion vs iteration trade-offs
- [ ] Debug tree recursion issues quickly

### **Progress Tracking**
- [ ] **Problems Solved**: ___/20+ problems completed
- [ ] **Time Investment**: ___/25+ hours practiced
- [ ] **Mock Interviews**: ___/3 tree focused sessions
- [ ] **Confidence Level**: ___/10 (Rate your confidence 1-10)

## 🎖️ **Success Metrics**
- ✅ Master all three traversal methods (recursive, iterative, Morris)
- ✅ Solve tree problems using recursion confidently
- ✅ Handle BST-specific optimizations
- ✅ Construct trees from different traversal combinations
- ✅ Explain time/space complexity for tree operations

---

**Previous**: [← Linked Lists](../06_linked_lists/) | **Next**: [Tries →](../08_tries/)
