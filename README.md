<h1 align="center"> Data-Structures-and-Algorithmns</h1>

# Data structures

## 1. Arrays

Arrays are a collection of items stored at contiguous memory locations.

*Advantages:*

1. Easy to implement: Arrays are simple to implement and use.
2. Fast access: Elements can be accessed quickly using their index. - O(1) time complexity.
3. Easy to append: Adding elements at the end is straightforward. - O(1) time complexity on average.

*Disadvantages:*

1. Inefficient insertions/deletions: Adding or removing elements can be slow, as it may require shifting elements. - O(n) time complexity.

*Usage:*

1. Traverse a structure in order.
2. Acess specific elements quickly through indexing.
3. Compare elements from both ends of the array.
4. Sliding window problems.

## 2. Strings

Strings are a sequence of characters, often used to represent text.

*Advantages:*

1. Appendable: Strings can be easily concatenated or appended to form new strings.
2. Easy to manipulate: Many built-in functions are available for string manipulation, such as slicing, searching, and replacing.
3. Readable: Strings are human-readable and can be easily understood and modified.

*Disadvantages:*

1. Immutable: Strings cannot be changed after creation, which can lead to inefficiencies when modifying them.
2. Modifying strings can be costly: Since strings are immutable, any modification creates a new string, which can be inefficient in terms of both time and space.

*Usage:*

1. Find longest substring without repeating characters.
2. Check if 2 strings are anagrams.
3. Return all substrings that match a given pattern.

## 3. Sets

Sets are a collection of unique items, often used to store non-repeating elements. It hashes elements then when during searching it again do hash and after that it goes to the index of that hash.

*Advantages:*

1. Fast membership testing: Sets provide O(1) average time complexity for membership tests (checking if an element is in the set).
2. Unique elements: Sets automatically handle duplicates, ensuring all elements are unique.
3. Mathematical set operations: Sets support operations like union, intersection, and difference.

*Disadvantages:*

1. Unordered: Sets do not maintain any specific order of elements.
2. Higher memory usage: Sets may use more memory than lists or arrays due to the overhead of hashing.

*Usage:*

1. Remove duplicates from a collection.
2. Check for membership in a collection.
3. Perform mathematical set operations.

## 5. Hash Maps

Hash maps are a data structure that stores key-value pairs, allowing for fast retrieval of values based on their keys. They use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

*Advantages:*

1. Fast access: Hash maps provide O(1) average time complexity for lookups, insertions, and deletions.
2. Flexible keys: Keys can be of any immutable type, allowing for a wide range of applications.
3. Efficient memory usage: Hash maps can be more memory-efficient than other data structures like trees or linked lists.
   
*Disadvantages:*

1. Collision handling: When two keys hash to the same index, it can lead to collisions, which can degrade performance.
2. Unordered: Hash maps do not maintain the order of elements.
3. Memory overhead: Hash maps may use more memory than other data structures due to the need for storing keys and values, as well as handling collisions.

*Usage:*

1. Implementing caches (e.g., LRU cache).
2. Counting occurrences of elements (e.g., word frequency).
3. Grouping anagrams or similar items.

---

<span style='color:skyblue'>Note</span>: Rule of thumb

- Input ~ 10^4: use O(n^2) algorithms or less.
- Input ~ 10^5: use O(n log n) algorithms or less.