class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        newRanges = []
        points.sort()
        for x1, x2 in points:
            if not newRanges or x1 > newRanges[-1][1]:
                newRanges.append([x1, x2])
            else:
                newRanges[-1] = [newRanges[-1][0], min(newRanges[-1][1], x2)]
        
        return len(newRanges)