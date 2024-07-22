class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
# 1. no overlaps and merging
#     old[end] < new[start]
# 2. overlaps and merging
#     new[end] >= old[start]
# 3. remaining
#     append(old)
        i = 0
        N = len(intervals)
        res = []

        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < N and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        
        while i < N:
            res.append(intervals[i])
            i += 1
        
        return res