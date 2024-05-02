from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_positive = -1
        
        for num in nums:
            if -num in nums and num > max_positive:
                max_positive = num
        
        return max_positive

        