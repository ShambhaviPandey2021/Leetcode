from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        index = 0
        
        while index < n and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1
        
        while index < n and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        
        result.append(newInterval)
        result.extend(intervals[index:])
        
        return result
