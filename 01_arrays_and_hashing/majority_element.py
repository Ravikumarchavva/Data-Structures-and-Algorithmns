from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        balance = 0
        candidate = None

        for num in nums:
            if balance == 0:
                candidate = num
            if num == candidate:
                balance += 1
            else:
                balance -= 1

        return candidate
