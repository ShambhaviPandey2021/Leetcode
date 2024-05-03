class Solution:
    @staticmethod
    def compareVersion(version1: str, version2: str) -> int:
        revs1 = version1.split('.')
        revs2 = version2.split('.')
        i = 0
        while i < max(len(revs1), len(revs2)):
            v1 = int(revs1[i]) if i < len(revs1) else 0
            v2 = int(revs2[i]) if i < len(revs2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            i += 1
        return 0
