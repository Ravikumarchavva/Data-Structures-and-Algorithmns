class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].remove((k,v))
        return

        

if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)          # The map is now [[1,1]]
    myHashMap.put(2, 2)          # The map is now [[1,1], [2,2]]
    print(myHashMap.get(1))      # return 1, The map is now [[1,1], [2,2]]
    print(myHashMap.get(3))      # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1)          # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    print(myHashMap.get(2))      # return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2)          # remove the mapping for 2, The map is now [[1,1]]
    print(myHashMap.get(2))      # return -1 (i.e., not found), The map is now [[1,1]]