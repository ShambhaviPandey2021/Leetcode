# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        child_nodes = set()
        
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            child_nodes.add(child_val)
        
        root = None
        for parent_val in nodes:
            if parent_val not in child_nodes:
                root = nodes[parent_val]
                break
                
        return root        