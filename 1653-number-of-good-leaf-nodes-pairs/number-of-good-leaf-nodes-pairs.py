# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node, leaf_count_at_depth, current_depth):
            if node is None or current_depth >= distance:
                return

            if node.left is None and node.right is None:
                leaf_count_at_depth[current_depth] += 1
                return
            dfs(node.left, leaf_count_at_depth, current_depth + 1)
            dfs(node.right, leaf_count_at_depth, current_depth + 1)

        if root is None:
            return 0
        total_pairs = self.countPairs(root.left, distance) + self.countPairs(root.right, distance)
      
        left_leaf_count = Counter()
        right_leaf_count = Counter()
        dfs(root.left, left_leaf_count, 1)
        dfs(root.right, right_leaf_count, 1)

        for depth_left, count_left in left_leaf_count.items():
            for depth_right, count_right in right_leaf_count.items():
                if depth_left + depth_right <= distance:
                    total_pairs += count_left * count_right

        return total_pairs
