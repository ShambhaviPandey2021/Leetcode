class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        
        def dfs(ring_idx, key_idx):
            if key_idx == len(key):
                return 0
            
            if (ring_idx, key_idx) in memo:
                return memo[(ring_idx, key_idx)]
            
            min_steps = float('inf')
            for i in range(len(ring)):
                if ring[i] == key[key_idx]:
                    steps = min(abs(i - ring_idx), len(ring) - abs(i - ring_idx))
                    steps += dfs(i, key_idx + 1)
                    min_steps = min(min_steps, steps)
            
            memo[(ring_idx, key_idx)] = min_steps
            return min_steps
        
        return dfs(0, 0) + len(key)
