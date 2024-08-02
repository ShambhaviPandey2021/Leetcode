class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        n = len(nums)
        
        if total_ones == 0:
            return 0
        extended_nums = nums + nums
        current_ones_in_window = sum(extended_nums[:total_ones])
        max_ones_in_window = current_ones_in_window
        
        for i in range(1, n):
            current_ones_in_window += extended_nums[i + total_ones - 1] - extended_nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        min_swaps = total_ones - max_ones_in_window
        return min_swaps
        