class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidates = 0;
        for(int num : nums ){
            if(count == 0){
                candidates = num;
            }
            count += (num == candidates) ? 1 : -1;
        }
        return candidates;
    }
};