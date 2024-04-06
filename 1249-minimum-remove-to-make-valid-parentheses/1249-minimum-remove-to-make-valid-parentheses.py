class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for c in s:
            if c == "(":
                res.append(c)
                count = count + 1 
            elif c == ")" and count>0:
                res.append(c)
                count = count -1
            elif c != ")":
                res.append(c)
        filter = []
        for c in res[::-1]:
            if c == "(" and count>0:
                count -= 1
            else:
                filter.append(c)
        return "".join(filter[::-1])
                