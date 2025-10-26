from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                self.dp[r+1][c+1] = matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
    
if __name__ == "__main__":
    numMatrix = NumMatrix([[3,0,1,4,2],
                            [5,6,3,2,1],
                            [1,2,0,1,5],
                            [4,1,0,1,7],
                            [1,0,3,0,5]])
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
    print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
    print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12