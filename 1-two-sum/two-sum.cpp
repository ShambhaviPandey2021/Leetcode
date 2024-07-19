class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>res;
        unordered_map<int , int> mpp;

        for(int j = 0;j<nums.size();j++){
            int complement = target -  nums[j];
            if(mpp.find(complement) != mpp.end()){
                res.push_back(mpp[complement]);
                res.push_back(j);
                return res;
            }
            mpp[nums[j]] = j;
         }
        return res;
    }
};