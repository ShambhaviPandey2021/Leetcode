class Solution:
    def myAtoi(self, s: str) -> int:
            i, sign, result = 0, 1, 0

            s = s.strip()

            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                if s[i] == '-':
                    sign = -1
                i += 1

            while i < len(s) and s[i].isdigit():
                digit = int(s[i])
                if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                    return -2**31 if sign == -1 else 2**31 - 1
                result = result * 10 + digit
                i += 1

            return sign * result


        