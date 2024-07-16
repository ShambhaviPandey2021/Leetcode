/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    string getDirections(TreeNode* root, int s, int d) {
        bool sm = false, dm = false; 
        int cnt = 0;
        string ans;
        function<void(TreeNode*, bool)> dfs = [&](TreeNode *root, bool isLeftChild) {
            if (cnt == 2 || !root) return; 
            int init = cnt;
            if (sm) ans += isLeftChild ? "L" : "R";
            else if (dm) ans += "U";
            if (root->val == s) {
                sm = true;
                ++cnt;
            } else if (root->val == d) {
                dm = true;
                ++cnt;
            }
            dfs(root->left, true);
            dfs(root->right, false);
      
            if (init == 0 && cnt == 1) { // If we met the first node
                if (sm) ans += "U"; // If it's source, add `U`
                else ans += isLeftChild ? "L" : "R"; // If it's dest, add `L/R`
            } else if (cnt == init && ans.size()) ans.pop_back(); 
        };
        dfs(root, false);
        if (ans.back() == 'U') reverse(begin(ans), end(ans));
        return ans;
    }
};
