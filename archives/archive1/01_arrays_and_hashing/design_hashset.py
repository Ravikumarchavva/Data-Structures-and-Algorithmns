class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return key in self.buckets[index]
        


if __name__ == "__main__":
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))  # returns True
    print(hashSet.contains(3))  # returns False (not found)
    hashSet.add(2)
    print(hashSet.contains(2))  # returns True
    hashSet.remove(2)
    print(hashSet.contains(2))  # returns False (already removed)