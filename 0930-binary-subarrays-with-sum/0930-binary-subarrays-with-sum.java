import java.util.HashMap;

class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int count = 0;
        HashMap<Integer, Integer> prefixSumCount = new HashMap<>();
        prefixSumCount.put(0, 1);
        int prefixSum = 0;
        
        for (int num : nums) {
            prefixSum += num;
            count += prefixSumCount.getOrDefault(prefixSum - goal, 0);
            prefixSumCount.put(prefixSum, prefixSumCount.getOrDefault(prefixSum, 0) + 1);
        }
        
        return count;
    }
}




