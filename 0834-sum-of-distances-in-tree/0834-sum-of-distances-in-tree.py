from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        subtree_sizes = [0] * n
        dist_sum = [0] * n
    
        def dfs1(node, parent):
            subtree_sizes[node] = 1
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    subtree_sizes[node] += subtree_sizes[neighbor]
                    dist_sum[node] += dist_sum[neighbor] + subtree_sizes[neighbor]
        
        dfs1(0, -1)  
        
        def dfs2(node, parent):
            for neighbor in adj_list[node]:
                if neighbor != parent:
                   
                    dist_sum[neighbor] = dist_sum[node] - subtree_sizes[neighbor] + (n - subtree_sizes[neighbor])
                    dfs2(neighbor, node)
        
        dfs2(0, -1) 
        
        return dist_sum
