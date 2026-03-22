from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low = low + 1
                mid = mid + 1
            
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1


if __name__ == "__main__":
    solution = Solution()
    arr = [2,0,2,1,1,0]
    solution.sortColors(arr)
    print(arr)  # Output should be [0,0,1,1,2,2]