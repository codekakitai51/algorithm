class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        L = len(intervals)
        if L == 1:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        prev = 0

        for cur in range(1, L):
            if intervals[prev][1] > intervals[cur][0]:
                count += 1
            else:
                prev = cur

        return count