class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            compared = res[-1]
            if compared[1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(compared[1], intervals[i][1])
        
        return res