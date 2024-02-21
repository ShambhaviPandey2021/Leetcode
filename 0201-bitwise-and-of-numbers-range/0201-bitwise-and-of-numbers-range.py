class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_right = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift_right += 1
        return left << shift_right
