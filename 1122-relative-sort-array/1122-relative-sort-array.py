from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        
        result = []
        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]
        
        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])
        remaining.sort()
     
        result.extend(remaining)
        
        return result
            
            
        
        
        