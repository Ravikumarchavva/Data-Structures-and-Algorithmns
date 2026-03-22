from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        hashset = set(nums)
        for i in range(1, n + 1):
            if i not in hashset:
                return i
    
if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))
    print(s.firstMissingPositive([3,4,-1,1]))
    print(s.firstMissingPositive([7,8,9,11,12]))