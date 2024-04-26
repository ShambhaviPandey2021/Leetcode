class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(n):
    
                dp[i][j] = grid[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])

        return min(dp[-1])
