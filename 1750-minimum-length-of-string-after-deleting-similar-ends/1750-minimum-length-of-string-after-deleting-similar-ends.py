class Solution:
    def minimumLength(self, s: str) -> int:
        def min_length(s: str) -> int:
            n = len(s)
            left = 0
            right = n - 1

            while left < right and s[left] == s[right]:
                while left + 1 < right and s[left] == s[left + 1]:
                    left += 1
                while right - 1 > left and s[right] == s[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            return max(right - left + 1, 0)
        
        return min_length(s)
