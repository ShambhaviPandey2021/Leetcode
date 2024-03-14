class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            count += prefix_sum_count[prefix_sum - goal]
            prefix_sum_count[prefix_sum] += 1
        
        return count
