# Bit Manipulation 🔢

> **Interview Frequency**: 30% | **Difficulty**: ⭐⭐⭐⭐ | **Pattern Priority**: #17

## 🎯 **Core Concept**
Bit manipulation involves direct manipulation of bits using bitwise operations. It's essential for optimizing space and time complexity, and crucial for systems programming and algorithmic problem-solving.

## 🏢 **Company Focus**
- **Google**: System optimization, search algorithms
- **Meta**: Memory optimization, data compression
- **Amazon**: System design, performance optimization
- **Apple**: Hardware-software optimization, embedded systems
- **Netflix**: Video encoding, data compression
- **Microsoft**: Operating systems, compiler optimizations

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR Properties | All FAANG |
| [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | Bit Counting | Google, Meta |
| [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | Single Bit Check | Apple, Amazon |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | Bit Reversal | Netflix, Microsoft |
| [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | XOR Finding | All FAANG |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Insight | Time | Space |
|---------|------------|-------------|------|-------|
| [Single Number II](https://leetcode.com/problems/single-number-ii/) | Medium | Bit Counting Modulo | O(N) | O(1) |
| [Bitwise AND Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium | Common Prefix | O(log N) | O(1) |
| [Maximum XOR](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Trie + Greedy | O(N log M) | O(N log M) |
| [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | Bit Addition | O(log N) | O(1) |
| [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | DP with Bits | O(N) | O(N) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Maximum XOR With Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) | Hard | Trie + Binary Search |
| [Minimum XOR Sum of Two Arrays](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) | Hard | Bitmask DP |
| [Count Number of Maximum XOR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) | Medium | Subset Generation |

## 🛠️ **Core Operations & Templates**

### **Fundamental Bit Operations**
```python
class BitOperations:
    """Essential bit manipulation operations"""
    
    @staticmethod
    def set_bit(num, i):
        """Set bit at position i"""
        return num | (1 << i)
    
    @staticmethod
    def clear_bit(num, i):
        """Clear bit at position i"""
        return num & ~(1 << i)
    
    @staticmethod
    def toggle_bit(num, i):
        """Toggle bit at position i"""
        return num ^ (1 << i)
    
    @staticmethod
    def get_bit(num, i):
        """Get bit at position i"""
        return (num >> i) & 1
    
    @staticmethod
    def is_bit_set(num, i):
        """Check if bit at position i is set"""
        return (num & (1 << i)) != 0
    
    @staticmethod
    def count_set_bits(num):
        """Count number of set bits (Brian Kernighan's algorithm)"""
        count = 0
        while num:
            num &= num - 1  # Clear rightmost set bit
            count += 1
        return count
    
    @staticmethod
    def count_set_bits_builtin(num):
        """Using built-in function"""
        return bin(num).count('1')
    
    @staticmethod
    def rightmost_set_bit(num):
        """Get rightmost set bit"""
        return num & -num
    
    @staticmethod
    def clear_rightmost_set_bit(num):
        """Clear rightmost set bit"""
        return num & (num - 1)
    
    @staticmethod
    def is_power_of_two(num):
        """Check if number is power of two"""
        return num > 0 and (num & (num - 1)) == 0
    
    @staticmethod
    def next_power_of_two(num):
        """Find next power of two"""
        if num <= 1:
            return 1
        
        num -= 1
        num |= num >> 1
        num |= num >> 2
        num |= num >> 4
        num |= num >> 8
        num |= num >> 16
        return num + 1
    
    @staticmethod
    def reverse_bits_32(num):
        """Reverse bits in 32-bit integer"""
        result = 0
        for _ in range(32):
            result = (result << 1) | (num & 1)
            num >>= 1
        return result
    
    @staticmethod
    def swap_bits(num, i, j):
        """Swap bits at positions i and j"""
        if ((num >> i) & 1) != ((num >> j) & 1):
            num ^= (1 << i) | (1 << j)
        return num

# Usage examples
bit_ops = BitOperations()
print(bit_ops.set_bit(5, 1))      # 7  (101 -> 111)
print(bit_ops.clear_bit(7, 1))    # 5  (111 -> 101)
print(bit_ops.count_set_bits(7))  # 3
print(bit_ops.is_power_of_two(8)) # True
```

### **Pattern 1: XOR Properties and Applications**
```python
def single_number(nums):
    """LC 136: Single Number - XOR all elements"""
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_ii(nums):
    """LC 137: Single Number II - appears 3 times except one"""
    ones = twos = 0
    
    for num in nums:
        # Update twos first, then ones
        twos ^= ones & num
        ones ^= num
        
        # Common bits in ones and twos should be cleared
        common = ones & twos
        ones ^= common
        twos ^= common
    
    return ones

def single_number_iii(nums):
    """LC 260: Single Number III - two numbers appear once"""
    # XOR all numbers to get XOR of two unique numbers
    xor_all = 0
    for num in nums:
        xor_all ^= num
    
    # Find rightmost set bit to separate the two numbers
    rightmost_set_bit = xor_all & -xor_all
    
    # Partition numbers into two groups and XOR each group
    num1 = num2 = 0
    for num in nums:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]

def missing_number(nums):
    """LC 268: Missing Number using XOR"""
    n = len(nums)
    result = n  # Start with n (the missing range endpoint)
    
    for i, num in enumerate(nums):
        result ^= i ^ num
    
    return result

def missing_number_math(nums):
    """Alternative using mathematical formula"""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_disappeared_numbers_xor(nums):
    """Find all disappeared numbers using XOR marking"""
    n = len(nums)
    
    # Mark numbers as negative by flipping sign at index
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    # Collect indices where numbers are still positive
    result = []
    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)
    
    return result

def maximum_xor_two_numbers(nums):
    """LC 421: Maximum XOR of Two Numbers (Greedy + Trie approach)"""
    max_xor = 0
    mask = 0
    
    # Build result bit by bit from most significant bit
    for bit in range(31, -1, -1):
        mask |= (1 << bit)
        prefixes = {num & mask for num in nums}
        
        candidate = max_xor | (1 << bit)
        
        # Check if we can achieve this candidate
        for prefix in prefixes:
            if candidate ^ prefix in prefixes:
                max_xor = candidate
                break
    
    return max_xor

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

def maximum_xor_trie(nums):
    """Maximum XOR using Trie data structure"""
    root = TrieNode()
    
    # Build trie
    for num in nums:
        node = root
        for bit in range(31, -1, -1):
            bit_val = (num >> bit) & 1
            if bit_val not in node.children:
                node.children[bit_val] = TrieNode()
            node = node.children[bit_val]
        node.value = num
    
    max_xor = 0
    
    # Find maximum XOR for each number
    for num in nums:
        node = root
        current_xor = 0
        
        for bit in range(31, -1, -1):
            bit_val = (num >> bit) & 1
            opposite_bit = 1 - bit_val
            
            if opposite_bit in node.children:
                current_xor |= (1 << bit)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit_val]
        
        max_xor = max(max_xor, current_xor)
    
    return max_xor
```

### **Pattern 2: Bit Counting and Analysis**
```python
def count_bits(n):
    """LC 338: Counting Bits - DP approach"""
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # dp[i] = dp[i >> 1] + (i & 1)
        dp[i] = dp[i // 2] + (i % 2)
    
    return dp

def count_bits_optimized(n):
    """Using Brian Kernighan's algorithm pattern"""
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    
    return dp

def hamming_weight(n):
    """LC 191: Number of 1 Bits"""
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

def hamming_distance(x, y):
    """LC 461: Hamming Distance"""
    return hamming_weight(x ^ y)

def total_hamming_distance(nums):
    """LC 477: Total Hamming Distance"""
    total = 0
    n = len(nums)
    
    # Count bits at each position
    for bit in range(32):
        ones = 0
        for num in nums:
            ones += (num >> bit) & 1
        
        zeros = n - ones
        total += ones * zeros
    
    return total

def bitwise_and_range(left, right):
    """LC 201: Bitwise AND of Numbers Range"""
    shift = 0
    
    # Find common prefix
    while left != right:
        left >>= 1
        right >>= 1
        shift += 1
    
    return left << shift

def range_sum_query_immutable_bit(nums):
    """Range sum using bit manipulation (Fenwick Tree)"""
    class BIT:
        def __init__(self, nums):
            self.n = len(nums)
            self.tree = [0] * (self.n + 1)
            
            for i, num in enumerate(nums):
                self.update(i, num)
        
        def update(self, i, delta):
            i += 1  # 1-indexed
            while i <= self.n:
                self.tree[i] += delta
                i += i & (-i)  # Add rightmost set bit
        
        def query(self, i):
            i += 1  # 1-indexed
            total = 0
            while i > 0:
                total += self.tree[i]
                i -= i & (-i)  # Remove rightmost set bit
            return total
        
        def range_sum(self, left, right):
            return self.query(right) - (self.query(left - 1) if left > 0 else 0)
    
    return BIT(nums)
```

### **Pattern 3: Arithmetic Operations with Bits**
```python
def add_without_plus(a, b):
    """LC 371: Sum of Two Integers without + operator"""
    while b != 0:
        carry = (a & b) << 1  # Calculate carry
        a = a ^ b             # Sum without carry
        b = carry             # New carry
    
    return a

def subtract_without_minus(a, b):
    """Subtraction using bit manipulation"""
    while b != 0:
        borrow = (~a & b) << 1
        a = a ^ b
        b = borrow
    
    return a

def multiply_without_multiply(a, b):
    """Multiplication using bit manipulation"""
    result = 0
    
    # Handle negative numbers
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)
    
    while b > 0:
        if b & 1:  # If b is odd
            result += a
        
        a <<= 1    # Double a
        b >>= 1    # Halve b
    
    return -result if negative else result

def divide_without_divide(dividend, divisor):
    """LC 29: Divide Two Integers"""
    # Handle overflow case
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    
    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    
    while dividend >= divisor:
        temp_divisor = divisor
        multiple = 1
        
        # Find largest multiple of divisor that fits in dividend
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        
        dividend -= temp_divisor
        quotient += multiple
    
    return -quotient if negative else quotient

def fast_power_bit(base, exponent):
    """Fast exponentiation using bit manipulation"""
    result = 1
    
    while exponent > 0:
        if exponent & 1:  # If exponent is odd
            result *= base
        
        base *= base
        exponent >>= 1
    
    return result

def gcd_bit(a, b):
    """GCD using bit manipulation (Stein's algorithm)"""
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Find common factors of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove factors of 2 from a
    while (a & 1) == 0:
        a >>= 1
    
    while b != 0:
        # Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1
        
        # Ensure a <= b
        if a > b:
            a, b = b, a
        
        b -= a
    
    return a << shift
```

### **Pattern 4: Subset and Combination Generation**
```python
def generate_all_subsets_bit(nums):
    """Generate all subsets using bit manipulation"""
    n = len(nums)
    subsets = []
    
    # Iterate through all possible bitmasks
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        subsets.append(subset)
    
    return subsets

def count_subsets_with_sum(nums, target):
    """Count subsets with given sum using bit manipulation"""
    n = len(nums)
    count = 0
    
    for mask in range(1 << n):
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):
                current_sum += nums[i]
        
        if current_sum == target:
            count += 1
    
    return count

def maximum_or_subset(nums):
    """LC 2044: Count Number of Maximum Bitwise-OR Subsets"""
    max_or = 0
    for num in nums:
        max_or |= num
    
    def count_subsets(index, current_or):
        if index == len(nums):
            return 1 if current_or == max_or else 0
        
        # Include current element
        include = count_subsets(index + 1, current_or | nums[index])
        # Exclude current element
        exclude = count_subsets(index + 1, current_or)
        
        return include + exclude
    
    return count_subsets(0, 0)

def beautiful_arrangement_bit(n):
    """LC 526: Beautiful Arrangement using bitmask"""
    def count_arrangements(mask, pos):
        if pos > n:
            return 1
        
        count = 0
        for i in range(1, n + 1):
            if not (mask & (1 << i)) and (pos % i == 0 or i % pos == 0):
                count += count_arrangements(mask | (1 << i), pos + 1)
        
        return count
    
    return count_arrangements(0, 1)

def traveling_salesman_bit(graph):
    """Traveling Salesman Problem using bitmask DP"""
    n = len(graph)
    memo = {}
    
    def tsp(mask, pos):
        if mask == (1 << n) - 1:  # Visited all cities
            return graph[pos][0]  # Return to start
        
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        
        result = float('inf')
        for next_city in range(n):
            if not (mask & (1 << next_city)):  # Not visited
                new_mask = mask | (1 << next_city)
                cost = graph[pos][next_city] + tsp(new_mask, next_city)
                result = min(result, cost)
        
        memo[(mask, pos)] = result
        return result
    
    return tsp(1, 0)  # Start from city 0
```

### **Pattern 5: Advanced Bit Manipulation**
```python
def reverse_bits(n):
    """LC 190: Reverse Bits"""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

def reverse_bits_optimized(n):
    """Optimized bit reversal using divide and conquer"""
    # Swap adjacent bits
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    # Swap adjacent pairs
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # Swap adjacent nibbles
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # Swap adjacent bytes
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # Swap adjacent 16-bit chunks
    n = (n >> 16) | (n << 16)
    
    return n & 0xFFFFFFFF

def utf8_validation(data):
    """LC 393: UTF-8 Validation"""
    remaining_bytes = 0
    
    for byte in data:
        if remaining_bytes == 0:
            # Determine how many bytes this character needs
            if (byte >> 5) == 0b110:      # 110xxxxx
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:   # 1110xxxx
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx
                remaining_bytes = 3
            elif (byte >> 7) != 0:        # Must be 0xxxxxxx for ASCII
                return False
        else:
            # Must be continuation byte: 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1
    
    return remaining_bytes == 0

def find_duplicate_number_bit(nums):
    """LC 287: Find Duplicate Number using bit manipulation"""
    n = len(nums) - 1
    duplicate = 0
    
    # Check each bit position
    for bit in range(32):
        count_base = 0
        count_nums = 0
        
        # Count set bits in range [1, n]
        for i in range(1, n + 1):
            if i & (1 << bit):
                count_base += 1
        
        # Count set bits in nums array
        for num in nums:
            if num & (1 << bit):
                count_nums += 1
        
        # If count in nums > count in base range, duplicate has this bit set
        if count_nums > count_base:
            duplicate |= (1 << bit)
    
    return duplicate

def gray_code(n):
    """LC 89: Gray Code"""
    result = [0]
    
    for i in range(n):
        # Mirror existing codes and add MSB
        mirror = [x | (1 << i) for x in reversed(result)]
        result.extend(mirror)
    
    return result

def gray_code_iterative(n):
    """Alternative iterative approach"""
    if n == 0:
        return [0]
    
    result = []
    for i in range(1 << n):
        # Gray code formula: i ^ (i >> 1)
        result.append(i ^ (i >> 1))
    
    return result
```

## 📊 **Bit Manipulation Complexity Analysis**

| Operation Type | Time Complexity | Space Complexity | Notes |
|----------------|----------------|------------------|-------|
| **Basic Operations** | O(1) | O(1) | Set, clear, toggle, get bit |
| **Bit Counting** | O(log N) / O(1) | O(1) | Kernighan's / built-in |
| **XOR Problems** | O(N) | O(1) | Single pass for most |
| **Subset Generation** | O(2^N × N) | O(2^N × N) | All subsets |
| **Bitmask DP** | O(2^N × N²) | O(2^N × N) | TSP, assignment |
| **Arithmetic Operations** | O(log N) | O(1) | Add, multiply, divide |

## 🧠 **Key Bit Manipulation Insights**

### **Essential Bit Properties**
- **XOR properties**: `a ^ a = 0`, `a ^ 0 = a`, commutative and associative
- **AND properties**: `a & (a-1)` clears rightmost set bit
- **OR properties**: `a | (a-1)` sets all bits to the right of rightmost set bit
- **Two's complement**: `-a = ~a + 1`

### **Common Bit Tricks**
- **Check power of 2**: `n > 0 && (n & (n-1)) == 0`
- **Get rightmost set bit**: `n & -n`
- **Clear rightmost set bit**: `n & (n-1)`
- **Set bit at position i**: `n | (1 << i)`
- **Clear bit at position i**: `n & ~(1 << i)`

### **Optimization Opportunities**
- **Space optimization**: Use bitmasks instead of arrays for small sets
- **Time optimization**: Bit operations are typically faster than arithmetic
- **Parallel processing**: Process multiple bits simultaneously

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Explain bit representation**: "Let me trace through the binary representation"
2. **Justify bit operations**: "XOR helps because it cancels out duplicates"
3. **Discuss edge cases**: "What happens with negative numbers or overflow?"

### **⚡ Optimization Techniques**
- **Use bit properties**: Leverage mathematical properties of bitwise operations
- **Avoid loops when possible**: Direct bit manipulation is often faster
- **Consider negative numbers**: Understand two's complement representation
- **Use built-in functions**: `bin()`, `bit_count()` when appropriate

### **🐛 Common Pitfalls**
- **Operator precedence**: Use parentheses around bit operations
- **Signed vs unsigned**: Be careful with negative numbers and shifts
- **Integer overflow**: Consider data type limits
- **Endianness**: Bit order in memory representation

## 🔍 **Problem Identification**

**Use Bit Manipulation when you see:**
- "Find single number" / "Find duplicate"
- "Count set bits" / "Hamming distance"
- "Subset generation" with small constraints
- "XOR" in problem statement
- "Power of two" checks
- "Optimize space" with boolean arrays
- "Implement arithmetic" without operators

## 📈 **Pattern Selection Guide**

### **Choose Based on Problem Requirements:**
1. **XOR patterns**: Single number, missing number, duplicate finding
2. **Bit counting**: Hamming weight, distance calculations
3. **Subset enumeration**: When n ≤ 20-25 elements
4. **Arithmetic simulation**: When operators are restricted
5. **Space optimization**: Boolean flags, state compression
6. **Advanced algorithms**: When direct bit manipulation provides elegance

## 📚 **Practice Schedule**

### **Week 1: Fundamentals**
- Day 1-2: Basic bit operations (set, clear, toggle, get)
- Day 3-4: XOR properties and applications
- Day 5-7: Bit counting and analysis problems

### **Week 2: Intermediate**
- Day 1-3: Arithmetic operations with bits
- Day 4-5: Subset generation and enumeration
- Day 6-7: Bitmask dynamic programming

### **Week 3: Advanced**
- Complex bit manipulation algorithms
- System-level bit operations
- Performance optimization techniques
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Master fundamental bitwise operations
- ✅ Solve XOR-based problems efficiently
- ✅ Implement arithmetic operations with bits
- ✅ Use bitmasks for subset problems
- ✅ Optimize algorithms using bit manipulation

---

**Previous**: [← Math & Geometry](../16_math_and_geometry/) | **Completion**: 🎉 **All Topics Covered!** 🎉
