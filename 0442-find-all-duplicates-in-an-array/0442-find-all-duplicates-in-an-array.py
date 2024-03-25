from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for num in nums:
            index = abs(num) - 1  # Convert to 0-based index
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]

        # Restore the original array
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicates