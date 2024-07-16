class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0, right = 0;
        int n = nums.size();
        long long sum = 0;  
        int maxFrequency = 0; 

        while (right < n) {
            sum += nums[right];

            long long requiredSum = static_cast<long long>(nums[right]) * (right - left + 1);
            long long diff = requiredSum - sum;

            while (diff > k) {
                sum -= nums[left];
                left++;
                requiredSum = static_cast<long long>(nums[right]) * (right - left + 1);
                diff = requiredSum - sum;
            }
            maxFrequency = max(maxFrequency, right - left + 1);

            right++;
        }

        return maxFrequency;
    }
};