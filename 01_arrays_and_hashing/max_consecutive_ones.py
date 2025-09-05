from typing import List

def max_consecutive_ones(nums: List[bool]) -> int:
    max_count = 0
    current_count = 0

    for num in nums:
        if num:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

if __name__ == "__main__":
    print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
    print(max_consecutive_ones([0, 0, 0, 0]))