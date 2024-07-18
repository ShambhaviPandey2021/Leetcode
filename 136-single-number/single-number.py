class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for it in nums:
            res ^= it
        return res