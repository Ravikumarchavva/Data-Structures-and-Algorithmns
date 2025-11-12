from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []

        candidate_1, candidate_2= None, None
        count_1, count_2 = 0, 0

        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 +=1
            elif count_1 == 0:
                candidate_1, count_1 = num, 1
            elif count_2 == 0:
                candidate_2, count_2 = num, 1
            else:
                count_1 -= 1
                count_2 -= 1

        result = []
        for cand in [candidate_1, candidate_2]:
            if cand is not None and nums.count(cand) > len(nums) // 3:
                result.append(cand)
        return result
                

if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))            # Output: [3]
    print(sol.majorityElement([1,1,1,3,3,2,2,2]))  # Output: [1,2]