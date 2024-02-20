class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int missingNum = n;
        for (int i = 0; i < n; ++i) {
            missingNum ^= i ^ nums[i];
        }
        return missingNum;
    }
}
