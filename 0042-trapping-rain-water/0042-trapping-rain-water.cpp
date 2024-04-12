class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;

        int left = 0, right = n - 1;
        int max_left = 0, max_right = 0;
        int water = 0;

        while (left <= right) {
            if (height[left] <= height[right]) {
                max_left = max(max_left, height[left]);
                water += max_left - height[left];
                left++;
            } else {
                max_right = max(max_right, height[right]);
                water += max_right - height[right];
                right--;
            }
        }
    
        return water; 
    }
};
    