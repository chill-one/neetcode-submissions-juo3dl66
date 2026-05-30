class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.P = self.computePrefixSum(matrix)


    def computePrefixSum(self, arr):
        n, m = len(arr[0]), len(arr)
        preSum = [[0] * (n + 1) for _ in range(m+1)]
        
        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += arr[i][j]
                preSum[i+1][j+1] = prefix + preSum[i][j+1]
        return preSum

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.P[r2+1][c2+1] - self.P[r1][c2+1] - self.P[r2+1][c1] + self.P[r1][c1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)