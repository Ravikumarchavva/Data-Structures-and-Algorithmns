from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_counts = {0: 1}

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - k]
            prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1

        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))          # Output: 2
    print(sol.subarraySum([1,2,3], 3))          # Output: 2
    print(sol.subarraySum([1,-1,0], 0))         # Output: 3