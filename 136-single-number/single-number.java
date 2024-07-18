class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for( int it : nums) {
            res ^= it;
        }
        return res;
    }
}