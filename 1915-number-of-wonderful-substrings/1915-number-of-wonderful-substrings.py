class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = {0: 1}
        mask = 0
        result = 0
        
        for char in word:
            mask ^= 1 << (ord(char) - ord('a'))
            result += count.get(mask, 0)
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)
            count[mask] = count.get(mask, 0) + 1
        
        return result
