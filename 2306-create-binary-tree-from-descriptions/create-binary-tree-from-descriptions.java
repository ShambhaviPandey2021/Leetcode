/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodes = new HashMap<>();
        Set<Integer> childNodes = new HashSet<>();
        for (int[] description : descriptions) {
            int parentVal = description[0];
            int childVal = description[1];
            boolean isLeft = description[2] == 1;

            nodes.putIfAbsent(parentVal, new TreeNode(parentVal));
            nodes.putIfAbsent(childVal, new TreeNode(childVal));

            if (isLeft) {
                nodes.get(parentVal).left = nodes.get(childVal);
            } else {
                nodes.get(parentVal).right = nodes.get(childVal);
            }

            childNodes.add(childVal);
        }

        TreeNode root = null;
        for (int parentVal : nodes.keySet()) {
            if (!childNodes.contains(parentVal)) {
                root = nodes.get(parentVal);
                break;
            }
        }

        return root;
    }
}