class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int maxArea = 0;
        while(l<r){
            int left_height = height[l];
            int right_height = height[r];
            int min_height = min(left_height, right_height);
            maxArea = max(maxArea, min_height * (r - l)); 
            if(left_height < right_height){ 
                l++;
            }
            else {
                r--;
            }
        }
        return maxArea;
    }
};
        
