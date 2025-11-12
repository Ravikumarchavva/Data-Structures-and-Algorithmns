class ClimbingStairs:
    def climb_stairs(self, n: int) -> int:
        prev_1, prev_2 = 1, 1

        for _ in range(2, n + 1):
            curr = prev_1 + prev_2
            prev_2, prev_1 = prev_1, curr

        return curr
    
if __name__ == "__main__":
    stairs = ClimbingStairs()
    print(stairs.climb_stairs(2))  # Output: 2
    print(stairs.climb_stairs(3))  # Output: 3