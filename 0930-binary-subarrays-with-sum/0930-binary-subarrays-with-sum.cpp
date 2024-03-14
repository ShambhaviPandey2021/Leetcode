class Solution {
public:
        int numSubarraysWithSum(vector<int>& nums, int goal) {
        int count = 0;
        unordered_map<int, int> prefixSumCount;
        prefixSumCount[0] = 1;
        int prefixSum = 0;
        
        for (int num : nums) {
            prefixSum += num;
            count += prefixSumCount[prefixSum - goal];
            prefixSumCount[prefixSum]++;
        }
        
        return count;
    }
};