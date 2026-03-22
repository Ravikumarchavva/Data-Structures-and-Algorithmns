from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 4]))  # False
    print(contains_duplicate([1, 2, 3, 1]))  # True