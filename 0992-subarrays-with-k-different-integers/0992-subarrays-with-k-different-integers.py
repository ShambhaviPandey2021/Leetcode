from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(nums, k):
            counter = defaultdict(int)
            left, distinct_count, result = 0, 0, 0
            
            for right in range(len(nums)):
                if counter[nums[right]] == 0:
                    distinct_count += 1
                counter[nums[right]] += 1
                
                while distinct_count > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1
                
                result += right - left + 1
                
            return result
        
        return at_most_k(nums, k) - at_most_k(nums, k - 1)
