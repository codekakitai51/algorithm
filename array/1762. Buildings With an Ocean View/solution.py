class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque([])

        # edge case
        if len(heights) == 1:
            res.append(0)
            return res
        
        maxI = len(heights) - 1
        res.append(maxI) # last building always be included
        for j in range(len(heights) - 1, -1, -1):
            if heights[j] > heights[maxI]:
                maxI = j
                res.appendleft(j)

        return res