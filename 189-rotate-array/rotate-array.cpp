class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        
        k = k % n;
        
        vector<int>temp(n);
        
        int index = 0;
        for(int i = n - k; i < n; i++){
            temp[index] = nums[i];
            index++;
        }
        for(int i = 0 ; i<n-k ;i++){
            temp[index] = nums[i];
            index++;
        }
        
        for(int i = 0;i<n;i++){
            nums[i] = temp[i];
        }
    }
};