class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missingNum = n
        for i in range(len(nums)):
            missingNum ^= i ^ nums[i]
        return missingNum