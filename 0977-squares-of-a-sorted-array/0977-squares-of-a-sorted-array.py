class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        result = [0]* len(nums)
        for i in range (len(nums)-1,-1,-1):
            if (abs(nums[l])> abs(nums[r])):
                result[i] = nums[l]* nums[l]
                l+=1
            else:
                result[i] = nums[r]*nums[r]
                r-=1
        return result