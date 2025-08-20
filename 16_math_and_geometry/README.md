# Math & Geometry 🧮

> **Interview Frequency**: 25% | **Difficulty**: ⭐⭐⭐⭐ | **Pattern Priority**: #16

## 🎯 **Core Concept**
Mathematical and geometric problems require understanding of number theory, combinatorics, probability, coordinate geometry, and algorithmic mathematics to solve computational challenges efficiently.

## 🏢 **Company Focus**
- **Google**: Search algorithms, PageRank, geometric problems
- **Meta**: Computer graphics, AR/VR mathematics
- **Amazon**: Optimization algorithms, logistics mathematics
- **Apple**: Graphics processing, computational geometry
- **Netflix**: Recommendation algorithms, statistical modeling
- **Microsoft**: Graphics engines, numerical computing

## 📋 **Essential Problems**

### **🔥 Must-Know (Do First)**
| Problem | Difficulty | Pattern | Companies |
|---------|------------|---------|-----------|
| [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Cycle Detection | Google, Meta |
| [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | Exponentiation | All FAANG |
| [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | Binary Search Math | Apple, Amazon |
| [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | Number Systems | Meta, Microsoft |
| [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Matrix Traversal | Google, Amazon |

### **🎯 Core Interview Questions**
| Problem | Difficulty | Key Concept | Time | Space |
|---------|------------|-------------|------|-------|
| [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | Matrix Rotation | O(N²) | O(1) |
| [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | In-place Modification | O(MN) | O(1) |
| [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | Easy | Binary Search | O(log N) | O(1) |
| [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | Easy | Base Conversion | O(N) | O(1) |
| [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | Medium | Number Theory | O(log N) | O(1) |

### **🚀 Advanced Challenges**
| Problem | Difficulty | Advanced Concept |
|---------|------------|------------------|
| [Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/) | Medium | Geometric Simulation |
| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Stack + Geometry |
| [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) | Hard | Mathematical Pattern |

## 🛠️ **Core Patterns & Templates**

### **Pattern 1: Number Theory & Prime Numbers**
```python
def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def sieve_of_eratosthenes(n):
    """Find all primes up to n"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples as composite
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

def gcd(a, b):
    """Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y

def factorial_trailing_zeroes(n):
    """LC 172: Factorial Trailing Zeroes"""
    count = 0
    power_of_5 = 5
    
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count

def count_primes(n):
    """LC 204: Count Primes using Sieve"""
    if n <= 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)

def happy_number(n):
    """LC 202: Happy Number - cycle detection"""
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = n
    fast = get_next(n)
    
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1
```

### **Pattern 2: Exponentiation & Logarithms**
```python
def power_iterative(x, n):
    """LC 50: Pow(x, n) - iterative approach"""
    if n == 0:
        return 1
    
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    current_power = x
    
    while n > 0:
        if n % 2 == 1:  # If n is odd
            result *= current_power
        current_power *= current_power
        n //= 2
    
    return result

def power_recursive(x, n):
    """Recursive fast exponentiation"""
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_recursive(x, -n)
    
    if n % 2 == 0:
        half_power = power_recursive(x, n // 2)
        return half_power * half_power
    else:
        return x * power_recursive(x, n - 1)

def sqrt_binary_search(x):
    """LC 69: Sqrt(x) using binary search"""
    if x < 2:
        return x
    
    left, right = 2, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

def sqrt_newton_method(x):
    """Newton's method for square root"""
    if x < 2:
        return x
    
    # Start with initial guess
    guess = x
    
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    
    return int(guess)

def is_perfect_square(num):
    """LC 367: Valid Perfect Square"""
    if num < 1:
        return False
    
    left, right = 1, num
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def my_sqrt_float(x, precision=1e-6):
    """Square root with floating point precision"""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    if x == 0:
        return 0
    
    left, right = 0, max(1, x)
    
    while right - left > precision:
        mid = (left + right) / 2
        
        if mid * mid < x:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2
```

### **Pattern 3: Matrix Operations**
```python
def rotate_image_90_clockwise(matrix):
    """LC 48: Rotate Image 90 degrees clockwise in-place"""
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def rotate_image_layers(matrix):
    """Alternative approach using layer-by-layer rotation"""
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top element
            top = matrix[first][i]
            
            # Top = Left
            matrix[first][i] = matrix[last - offset][first]
            
            # Left = Bottom
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Bottom = Right
            matrix[last][last - offset] = matrix[i][last]
            
            # Right = Top
            matrix[i][last] = top

def set_matrix_zeroes(matrix):
    """LC 73: Set Matrix Zeroes in-place"""
    if not matrix or not matrix[0]:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/column should be zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Use first row and column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set zeros based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle first row and column
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

def spiral_matrix(matrix):
    """LC 54: Spiral Matrix"""
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            # Traverse left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            # Traverse up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

def generate_spiral_matrix(n):
    """LC 59: Spiral Matrix II"""
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Fill top row
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        # Fill right column
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Fill bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            # Fill left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    return matrix
```

### **Pattern 4: Coordinate Geometry**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """Euclidean distance between two points"""
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def manhattan_distance(p1, p2):
    """Manhattan distance between two points"""
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def robot_bounded_in_circle(instructions):
    """LC 1041: Robot Bounded In Circle"""
    x, y = 0, 0
    direction = 0  # 0: North, 1: East, 2: South, 3: West
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for instruction in instructions:
        if instruction == 'G':
            dx, dy = directions[direction]
            x += dx
            y += dy
        elif instruction == 'L':
            direction = (direction - 1) % 4
        elif instruction == 'R':
            direction = (direction + 1) % 4
    
    # Robot is bounded if:
    # 1. It returns to origin, OR
    # 2. It doesn't face north (will eventually return due to cycle)
    return (x == 0 and y == 0) or direction != 0

def largest_rectangle_histogram(heights):
    """LC 84: Largest Rectangle in Histogram"""
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

def maximal_rectangle(matrix):
    """LC 85: Maximal Rectangle"""
    if not matrix or not matrix[0]:
        return 0
    
    max_area = 0
    heights = [0] * len(matrix[0])
    
    for row in matrix:
        for j in range(len(row)):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        
        max_area = max(max_area, largest_rectangle_histogram(heights))
    
    return max_area

def convex_hull_graham_scan(points):
    """Graham scan algorithm for convex hull"""
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    # Find the bottom-most point (or left most in case of tie)
    start = min(points, key=lambda p: (p[1], p[0]))
    
    # Sort points by polar angle with respect to start point
    def polar_angle(p):
        import math
        return math.atan2(p[1] - start[1], p[0] - start[0])
    
    sorted_points = sorted(points, key=polar_angle)
    
    hull = []
    for point in sorted_points:
        # Remove points that make clockwise turn
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    
    return hull
```

### **Pattern 5: Number System Conversions**
```python
def roman_to_int(s):
    """LC 13: Roman to Integer"""
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        # If current character value is less than next, subtract it
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            total += roman_values[s[i]]
            i += 1
    
    return total

def int_to_roman(num):
    """LC 12: Integer to Roman"""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    
    for i, value in enumerate(values):
        count = num // value
        if count:
            result += symbols[i] * count
            num %= value
    
    return result

def excel_sheet_column_number(column_title):
    """LC 171: Excel Sheet Column Number"""
    result = 0
    
    for char in column_title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    
    return result

def excel_sheet_column_title(column_number):
    """LC 168: Excel Sheet Column Title"""
    result = ""
    
    while column_number > 0:
        column_number -= 1  # Convert to 0-indexed
        result = chr(ord('A') + column_number % 26) + result
        column_number //= 26
    
    return result

def base_conversion(num, from_base, to_base):
    """Convert number from one base to another"""
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2")
    
    # Convert to decimal first
    decimal = 0
    power = 0
    
    while num > 0:
        digit = num % 10
        if digit >= from_base:
            raise ValueError(f"Invalid digit {digit} for base {from_base}")
        decimal += digit * (from_base ** power)
        power += 1
        num //= 10
    
    # Convert from decimal to target base
    if decimal == 0:
        return 0
    
    result = 0
    power = 0
    
    while decimal > 0:
        result += (decimal % to_base) * (10 ** power)
        decimal //= to_base
        power += 1
    
    return result

def add_binary(a, b):
    """LC 67: Add Binary"""
    result = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        
        if i >= 0:
            total += int(a[i])
            i -= 1
        
        if j >= 0:
            total += int(b[j])
            j -= 1
        
        result = str(total % 2) + result
        carry = total // 2
    
    return result
```

### **Pattern 6: Mathematical Sequences & Patterns**
```python
def fibonacci_iterative(n):
    """Fibonacci using iteration"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_matrix_exponentiation(n):
    """Fibonacci using matrix exponentiation - O(log n)"""
    def matrix_multiply(A, B):
        return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        
        if power % 2 == 0:
            half_power = matrix_power(matrix, power // 2)
            return matrix_multiply(half_power, half_power)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    if n <= 1:
        return n
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    
    return result_matrix[0][1]

def pascal_triangle(num_rows):
    """LC 118: Pascal's Triangle"""
    triangle = []
    
    for i in range(num_rows):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
    
    return triangle

def pascal_triangle_row(row_index):
    """LC 119: Pascal's Triangle II - space optimized"""
    row = [1]
    
    for i in range(row_index):
        # Build next row from right to left
        row.append(1)
        for j in range(len(row) - 2, 0, -1):
            row[j] += row[j - 1]
    
    return row

def ugly_numbers(n):
    """LC 264: Ugly Number II"""
    ugly = [1]
    i2 = i3 = i5 = 0
    
    for _ in range(1, n):
        next_2 = ugly[i2] * 2
        next_3 = ugly[i3] * 3
        next_5 = ugly[i5] * 5
        
        next_ugly = min(next_2, next_3, next_5)
        ugly.append(next_ugly)
        
        if next_ugly == next_2:
            i2 += 1
        if next_ugly == next_3:
            i3 += 1
        if next_ugly == next_5:
            i5 += 1
    
    return ugly[n - 1]

def count_digit_one(n):
    """LC 233: Number of Digit One"""
    count = 0
    factor = 1
    
    while factor <= n:
        higher = n // (factor * 10)
        current = (n // factor) % 10
        lower = n % factor
        
        if current == 0:
            count += higher * factor
        elif current == 1:
            count += higher * factor + lower + 1
        else:
            count += (higher + 1) * factor
        
        factor *= 10
    
    return count
```

## 📊 **Mathematical Algorithm Complexity**

| Problem Type | Time Complexity | Space Complexity | Key Technique |
|--------------|----------------|------------------|---------------|
| **Prime Checking** | O(√N) | O(1) | Trial Division |
| **Sieve of Eratosthenes** | O(N log log N) | O(N) | Sieving |
| **Fast Exponentiation** | O(log N) | O(1) | Binary Exponentiation |
| **Matrix Operations** | O(N²) - O(N³) | O(N²) | In-place or Auxiliary |
| **GCD/LCM** | O(log min(a,b)) | O(1) | Euclidean Algorithm |
| **Number Conversion** | O(log N) | O(log N) | Base Mathematics |

## 🧠 **Key Mathematical Insights**

### **Number Theory Fundamentals**
- **Prime factorization**: Every integer has unique prime factorization
- **Modular arithmetic**: Useful for large number computations
- **GCD properties**: GCD(a,b) = GCD(b, a mod b)
- **Combinatorics**: Count arrangements and selections

### **Geometric Principles**
- **Coordinate geometry**: Distance, slopes, areas
- **Convex hull**: Smallest convex polygon containing all points
- **Line intersection**: Solve system of linear equations
- **Rotation matrices**: Transform coordinates

### **Optimization Techniques**
- **Fast exponentiation**: Reduce O(N) to O(log N)
- **Matrix exponentiation**: For recurrence relations
- **Sieving**: Precompute for multiple queries
- **Mathematical formulas**: Direct computation when possible

## 💡 **Interview Tips**

### **🗣️ Communication Strategy**
1. **Identify the mathematical pattern**: "This looks like a geometric sequence"
2. **Discuss edge cases**: "What happens with negative numbers or zero?"
3. **Explain optimizations**: "We can use fast exponentiation to reduce complexity"

### **⚡ Optimization Techniques**
- **Use mathematical properties**: Leverage known formulas and identities
- **Avoid floating point**: Use integer arithmetic when possible
- **Precomputation**: Sieve for multiple prime queries
- **Matrix exponentiation**: For linear recurrences

### **🐛 Common Pitfalls**
- **Integer overflow**: Use appropriate data types
- **Floating point precision**: Be careful with decimal comparisons
- **Negative number handling**: Consider sign changes in algorithms
- **Edge cases**: Zero, one, negative inputs

## 🔍 **Problem Identification**

**Use Math & Geometry when you see:**
- "Calculate/compute mathematical expression"
- "Geometric shapes and coordinates"
- "Number theory problems"
- "Matrix operations and transformations"
- "Prime numbers and factorization"
- "Angle calculations and rotations"

## 📈 **Algorithm Selection Guide**

### **Choose Based on Problem Type:**
1. **Prime problems**: Sieve for multiple queries, trial division for single
2. **Exponentiation**: Fast exponentiation for large powers
3. **Matrix problems**: In-place for space optimization
4. **Geometry**: Coordinate geometry for 2D problems
5. **Sequences**: Look for mathematical patterns
6. **Conversions**: Base mathematics and digit manipulation

## 📚 **Practice Schedule**

### **Week 1: Number Theory**
- Day 1-2: Prime numbers, GCD/LCM
- Day 3-4: Exponentiation and square roots
- Day 5-7: Number system conversions

### **Week 2: Geometry & Matrices**
- Day 1-3: Matrix operations and transformations
- Day 4-5: Coordinate geometry problems
- Day 6-7: Advanced geometric algorithms

### **Week 3: Advanced Topics**
- Mathematical sequences and patterns
- Complex optimization problems
- Computational geometry
- Mock interview practice

## 🎖️ **Success Metrics**
- ✅ Master fundamental number theory algorithms
- ✅ Implement efficient matrix operations
- ✅ Solve coordinate geometry problems
- ✅ Handle edge cases in mathematical computations
- ✅ Optimize algorithms using mathematical properties

---

**Previous**: [← Intervals](../15_intervals/) | **Next**: [Bit Manipulation →](../17_bit_manipulation/)
