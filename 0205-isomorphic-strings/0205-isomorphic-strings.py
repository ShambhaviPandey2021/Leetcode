class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        
        for s_char, t_char in zip(s, t):
            if s_char not in s_to_t and t_char not in t_to_s:
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char
            elif s_to_t.get(s_char) != t_char or t_to_s.get(t_char) != s_char:
                return False
        
        return True