
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        g = [[-1] * n for _ in range(n)]
        vis = [[False] * n for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        level = 0
        while q:
            t = []
            for coord in q:
                x, y = coord
                if x < 0 or y < 0 or x == n or y == n or g[x][y] != -1:
                    continue
                g[x][y] = level
                t.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
            q = t
            level += 1
            
        def dfs(i, j, v):
            if i < 0 or j < 0 or i == n or j == n or vis[i][j] or g[i][j] <= v:
                return False
            vis[i][j] = True
            return (
                (i == n - 1 and j == n - 1) or
                dfs(i + 1, j, v) or
                dfs(i, j + 1, v) or
                dfs(i - 1, j, v) or
                dfs(i, j - 1, v)
            )
        
        left, right = 0, level
        while left < right:
            for row in vis:
                for i in range(n):
                    row[i] = False
            mid = (left + right) >> 1
            if dfs(0, 0, mid):
                left = mid + 1
            else:
                right = mid
        
        return right
