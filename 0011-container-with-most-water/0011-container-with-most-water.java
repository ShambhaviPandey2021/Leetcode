class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length-1;
        int max = 0;
        while(l<r){
            int left_height = height[l];
            int right_height = height[r];
            int min_height = Math.min(left_height, right_height);
            max = Math.max(max, min_height * (r - l)); 
            if(left_height < right_height) l++;
            else r--;
        }
        return max;
    }
}