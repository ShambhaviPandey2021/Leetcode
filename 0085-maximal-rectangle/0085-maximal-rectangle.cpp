class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        vector<int> heights(cols, 0);
        int maxArea = 0;

        auto largestRectangleArea = [](vector<int>& heights) {
            stack<int> st;
            int maxArea = 0;
            int n = heights.size();
            
            for (int i = 0; i <= n; ++i) {
                int h = (i == n) ? 0 : heights[i];
                while (!st.empty() && heights[st.top()] > h) {
                    int height = heights[st.top()];
                    st.pop();
                    int width = st.empty() ? i : i - st.top() - 1;
                    maxArea = max(maxArea, height * width);
                }
                st.push(i);
            }
            
            return maxArea;
        };
        
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                heights[j] = (matrix[i][j] == '0') ? 0 : heights[j] + 1;
            }
            maxArea = max(maxArea, largestRectangleArea(heights));
        }
        
        return maxArea;
    }
};
