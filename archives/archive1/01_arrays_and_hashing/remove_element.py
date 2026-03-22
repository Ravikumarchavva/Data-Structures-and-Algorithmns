from typing import List


def removeElement(nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        
        return len(nums)

if __name__ == "__main__":
    print(removeElement([3,2,2,3], 3))