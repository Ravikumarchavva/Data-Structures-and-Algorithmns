from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        count = 0
        for i in range(l):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and ( i == l - 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
            if count >= n:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))
    print(s.canPlaceFlowers([1,0,0,0,1], 2))