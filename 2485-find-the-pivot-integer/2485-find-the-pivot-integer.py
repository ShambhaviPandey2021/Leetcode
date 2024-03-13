import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        a = math.sqrt(total_sum)

        if a - math.ceil(a) == 0:
            return int(a)
        else:
            return -1

