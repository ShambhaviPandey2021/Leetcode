from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        def get_neighbors(node):
            neighbors = []
            for i in range(4):
                for move in [-1, 1]:
                    new_digit = (int(node[i]) + move) % 10
                    neighbor = node[:i] + str(new_digit) + node[i+1:]
                    neighbors.append(neighbor)
            return neighbors
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps
            if node in deadends:
                continue
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
