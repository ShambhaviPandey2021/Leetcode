class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int []result= new int[n];

        int l = 0, r = n - 1, i = n - 1;
        while (l <= r) {
            int l_sq = nums[l] * nums[l];
            int r_sq = nums[r] * nums[r];
            if (l_sq > r_sq) {
                result[i--] = l_sq;
                l++;
            } else {
                result[i--] = r_sq;
                r--;
            }
        }
        
        return result;  
    }
}