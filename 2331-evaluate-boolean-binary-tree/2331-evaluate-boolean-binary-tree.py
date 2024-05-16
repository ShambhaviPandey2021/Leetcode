# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Helper function to evaluate a node
        def evaluate(node):
            if not node:
                return False
            if not node.left and not node.right:
                return bool(node.val)

            left_val = evaluate(node.left)
            right_val = evaluate(node.right)

            
            if node.val == 2:
                return left_val or right_val
            elif node.val == 3:
                return left_val and right_val

        return evaluate(root)
