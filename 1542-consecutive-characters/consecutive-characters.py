class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        count  =  1
        maxCount = 1
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                maxCount = max(count , maxCount)
                count = 1
        maxCount = max(count, maxCount)
        return maxCount