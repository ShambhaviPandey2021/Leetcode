class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = collections.Counter(s)
        string = []
        for char in order:
            if char in s_count:
                string.extend([char]*s_count[char])
                del s_count[char]
        for char , count in s_count.items():
            string.extend([char]*s_count[char])
        return "".join(string)        