class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            gold = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            max_gold = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                max_gold = max(max_gold, dfs(x, y))
            grid[i][j] = gold  # Revert the mark
            return max_gold + gold
        
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold
