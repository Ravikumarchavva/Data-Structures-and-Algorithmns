# Tries (Prefix Trees) 🌲

> **Interview Frequency**: 40% | **Difficulty**: ⭐⭐ | **Pattern Priority**: #8

## 🎯 **Core Concept**
Tries are tree-like data structures that store strings efficiently by sharing common prefixes. Essential for string matching, auto-complete, and word search problems.

## 🏢 **Company Focus**
- **Google**: Search autocomplete, spell checkers
- **Meta**: Hashtag suggestions, user search
- **Amazon**: Product search, recommendation systems
- **Apple**: Siri voice recognition, predictive text
- **Microsoft**: Word processors, search engines

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Basic Trie Operations | All FAANG |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie + DFS | Google, Meta |
| [Add and Search Word](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie with Wildcards | Amazon, Apple |
| [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | Prefix Matching | Google, Microsoft |
| [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Medium | Trie Construction | Apple |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Word Break II](https://leetcode.com/problems/word-break-ii/) | Hard | Trie + Backtracking | O(n³) | O(n³) |
| [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Hard | Trie + Palindrome Check | O(n×m²) | O(n×m) |
| [Maximum XOR](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Binary Trie | O(n×log(max)) | O(n×log(max)) |
| [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | Trie with Values | O(m) | O(ALPHABET_SIZE×N×M) |
| [Word Squares](https://leetcode.com/problems/word-squares/) | Hard | Trie + Backtracking | O(n×26^L) | O(n×L) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Stream of Characters](https://leetcode.com/problems/stream-of-characters/) | Hard | Reverse Trie + Streaming |
| [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Hard | Trie + DP |
| [Design Search Autocomplete](https://leetcode.com/problems/design-search-autocomplete-system/) | Hard | Trie + Ranking System |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Basic Trie Implementation**
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks end of a word
        self.word = None  # Optional: store the actual word
        self.value = 0  # Optional: for storing values (like frequency)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.word = word  # Store the word at the end
    
    def search(self, word):
        """Search for a word in the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word starts with the given prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def get_words_with_prefix(self, prefix):
        """Get all words that start with the given prefix"""
        node = self.root
        
        # Navigate to the prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # DFS to find all words from this node
        words = []
        self._dfs_words(node, prefix, words)
        return words
    
    def _dfs_words(self, node, current_word, words):
        """Helper function to collect all words from a node"""
        if node.is_end_of_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs_words(child_node, current_word + char, words)
```

### **Pattern 2: Trie with Wildcards (Design Add and Search)**
```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        """Add a word to the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Search word with possible wildcard '.' characters"""
        return self._search_helper(word, 0, self.root)
    
    def _search_helper(self, word, index, node):
        """Recursive helper for wildcard search"""
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._search_helper(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character
            if char not in node.children:
                return False
            return self._search_helper(word, index + 1, node.children[char])
```

### **Pattern 3: Trie for Grid Word Search**
```python
def find_words(board, words):
    """Word Search II - Find all words in 2D board"""
    # Build trie from words
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result = set()
    
    def dfs(row, col, node, visited):
        # Check bounds and if cell is visited
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            (row, col) in visited):
            return
        
        char = board[row][col]
        if char not in node.children:
            return
        
        node = node.children[char]
        
        # Found a word
        if node.is_end_of_word:
            result.add(node.word)
        
        # Mark as visited and explore neighbors
        visited.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            dfs(row + dr, col + dc, node, visited)
        
        # Backtrack
        visited.remove((row, col))
    
    # Try starting from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie.root, set())
    
    return list(result)
```

### **Pattern 4: Binary Trie (for XOR problems)**
```python
class BinaryTrieNode:
    def __init__(self):
        self.children = {}  # 0 or 1
        self.value = None

class BinaryTrie:
    def __init__(self, max_bits=32):
        self.root = BinaryTrieNode()
        self.max_bits = max_bits
    
    def insert(self, num):
        """Insert a number into binary trie"""
        node = self.root
        
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            
            if bit not in node.children:
                node.children[bit] = BinaryTrieNode()
            
            node = node.children[bit]
        
        node.value = num
    
    def find_max_xor(self, num):
        """Find number that gives maximum XOR with given number"""
        node = self.root
        
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction for maximum XOR
            toggle_bit = 1 - bit
            
            if toggle_bit in node.children:
                node = node.children[toggle_bit]
            elif bit in node.children:
                node = node.children[bit]
            else:
                return 0  # Trie is empty
        
        return num ^ node.value

def find_maximum_xor(nums):
    """Find maximum XOR of any two numbers in array"""
    trie = BinaryTrie()
    max_xor = 0
    
    for num in nums:
        trie.insert(num)
        max_xor = max(max_xor, trie.find_max_xor(num))
    
    return max_xor
```

### **Pattern 5: Trie with Frequency/Values**
```python
class MapSum:
    """Map Sum Pairs - Trie with sum values"""
    def __init__(self):
        self.root = TrieNode()
        self.map = {}  # Store key-value pairs
    
    def insert(self, key, val):
        """Insert key-value pair"""
        # Calculate difference for existing keys
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        # Update trie with delta
        node = self.root
        node.value += delta
        
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += delta
    
    def sum(self, prefix):
        """Get sum of all values with given prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.value
```

## 📊 **Trie vs Other Data Structures**

| Operation | Trie | Hash Map | Binary Search Tree |
|-----------|------|----------|-------------------|
| **Insert** | O(m) | O(1) avg | O(log n) |
| **Search** | O(m) | O(1) avg | O(log n) |
| **Prefix Search** | O(p) | O(n) | O(n) |
| **Memory** | O(ALPHABET × N × M) | O(n) | O(n) |
| **Ordered Traversal** | Yes | No | Yes |

Where: m = word length, p = prefix length, n = number of words

## 🧠 **Key Insights**

### **When to Use Tries**
- **Prefix operations**: Auto-complete, spell checkers
- **Word games**: Boggle, word search puzzles
- **String matching**: Multiple pattern matching
- **IP routing**: Longest prefix matching

### **Trie Advantages**
- **Prefix queries**: Very efficient for prefix-based operations
- **Memory sharing**: Common prefixes stored once
- **Lexicographic order**: Natural alphabetical ordering
- **No hash collisions**: Unlike hash maps

### **Trie Disadvantages**
- **Memory intensive**: Each node stores multiple pointers
- **Cache performance**: Poor locality compared to arrays
- **Limited use cases**: Mainly for string problems

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Explain structure**: "Trie shares common prefixes efficiently"
2. **Discuss space trade-off**: "Uses more memory for faster prefix operations"
3. **Mention alternatives**: "Could use hash map but lose prefix benefits"

### **⚡ Optimization Techniques**
- **Compressed tries**: Merge nodes with single child
- **Array vs HashMap**: Use array for small alphabets (26 letters)
- **Lazy deletion**: Mark nodes instead of actually deleting

### **🐛 Common Pitfalls**
- **Memory leaks**: Properly deallocate nodes when deleting
- **Case sensitivity**: Handle uppercase/lowercase consistently
- **Character encoding**: Consider Unicode vs ASCII
- **End marker**: Don't forget to mark word endings

## 🔍 **Problem Identification**

**Use Trie when you see:**
- "Auto-complete" or "suggestions"
- "Prefix matching"
- "Word search" in 2D grid
- "Dictionary" of words
- "Replace words" with shorter forms
- Multiple string pattern matching

## 📈 **Complexity Analysis**

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Build Trie** | O(N × M) | O(ALPHABET × N × M) | N words, M avg length |
| **Search Word** | O(M) | O(1) | M = word length |
| **Prefix Search** | O(P + K) | O(1) | P = prefix, K = results |
| **Insert/Delete** | O(M) | O(M) worst case | New nodes created |
| **DFS Traversal** | O(N × M) | O(M) recursion | Visit all words |

## 🎯 **Advanced Trie Applications**

### **Auto-complete System**
```python
class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.current_sentence = ""
        
        # Build trie with frequency data
        for i, sentence in enumerate(sentences):
            node = self.trie.root
            for char in sentence:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
            node.frequency = times[i]
    
    def input(self, c):
        if c == '#':
            # End of sentence - save it
            self._save_sentence()
            self.current_sentence = ""
            return []
        
        self.current_sentence += c
        return self._get_suggestions()
    
    def _get_suggestions(self):
        # Find all sentences with current prefix
        node = self.trie.root
        for char in self.current_sentence:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all sentences and sort by frequency/lexicographic
        suggestions = []
        self._collect_sentences(node, self.current_sentence, suggestions)
        
        # Sort by frequency (desc) then lexicographically (asc)
        suggestions.sort(key=lambda x: (-x[1], x[0]))
        
        return [sentence for sentence, freq in suggestions[:3]]
```

## 📚 **Practice Schedule**

### **Week 1: Foundation**
- Day 1-2: Implement Trie (Prefix Tree)
- Day 3-4: Add and Search Word (with wildcards)
- Day 5-7: Replace Words, Longest Word in Dictionary

### **Week 2: Intermediate**
- Day 1-3: Word Search II (Trie + DFS)
- Day 4-5: Map Sum Pairs, Maximum XOR
- Day 6-7: Palindrome Pairs

### **Week 3: Advanced**
- Design Search Autocomplete System
- Stream of Characters
- Concatenated Words
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Implement basic trie with insert/search/prefix operations
- ✅ Handle wildcard characters in search
- ✅ Combine trie with DFS for grid problems
- ✅ Build binary trie for XOR problems
- ✅ Design efficient auto-complete systems

---

**Previous**: [← Trees](../07_trees/) | **Next**: [Heap/Priority Queue →](../09_heap_priority_queue/)
