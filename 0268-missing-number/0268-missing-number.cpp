#include <vector>

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int missingNum = n;
        for (int i = 0; i < n; ++i) {
            missingNum ^= i ^ nums[i];
        }
        return missingNum;
    }
};