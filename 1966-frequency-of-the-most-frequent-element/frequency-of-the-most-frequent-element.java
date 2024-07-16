import java.util.Arrays;

class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums); 
        int left = 0;
        int right = 0;
        int n = nums.length;
        long sum = 0; 

        int maxFrequency = 0;

        while (right < n) {
            sum += nums[right];

            long requiredSum = (long) nums[right] * (right - left + 1);
            long diff = requiredSum - sum;

            while (diff > k) {
                sum -= nums[left];
                left++;
                requiredSum = (long) nums[right] * (right - left + 1);
                diff = requiredSum - sum;
            }

            maxFrequency = Math.max(maxFrequency, right - left + 1);

            right++;
        }

        return maxFrequency;
    }
}

 