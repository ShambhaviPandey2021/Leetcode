class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int maximum = INT_MIN;
        int ansStart = -1;
        int ansEnd = -1;
        int sum = 0;
        int start = 0;

        for(int i = 0; i < n; i++) {
            if(sum == 0){
                start = i;
            }
            sum = sum + nums[i];
            if(sum > maximum){
                maximum = sum;
                ansStart = start;
                ansEnd = i;
            }
            if(sum < 0) {
                sum = 0;
            }
        }
        return maximum;
        
    }
};