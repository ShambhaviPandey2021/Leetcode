
class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int n = nums.length;
        int[] netChange = new int[n];
        long nodeSum = 0;

        for (int i = 0; i < n; i++) {
            netChange[i] = (nums[i] ^ k) - nums[i];
            nodeSum += nums[i];
        }

        Arrays.sort(netChange);

        for (int i = n-1; i >= 1; i -= 2) {
            // If netChange contains odd number of elements break the loop
            if (i - 1 == -1) {
                break;
            }
            long pairSum = netChange[i] + netChange[i - 1];
            // Include in nodeSum if pairSum is positive
            if (pairSum > 0) {
                nodeSum += pairSum;
            } else {
                return nodeSum;
            }
        }
        return nodeSum;
    }
}