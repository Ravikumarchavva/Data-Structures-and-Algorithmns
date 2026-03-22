from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold_price = 0
        hold = False
        for i in range(len(prices)):
            if i < len(prices) - 1:
                if prices[i+1] > prices[i]:
                    if not hold:
                        hold = True
                        hold_price = prices[i]
                else:
                    if hold:
                        profit += prices[i] - hold_price
                        hold=False
            else:
                if hold:
                    profit += prices[i] - hold_price
        return profit
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # Output: 7
    print(sol.maxProfit([1,2,3,4,5]))    # Output: 4
    print(sol.maxProfit([7,6,4,3,1]))    # Output: 0