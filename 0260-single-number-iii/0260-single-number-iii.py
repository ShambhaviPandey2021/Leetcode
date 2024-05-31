class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for n in nums:
            res ^= n

        mask = res & -res

        one = 0
        for n in nums:
            if n & mask == 0: # Bit not set
               one ^= n

        two = res ^ one
        return [one, two]