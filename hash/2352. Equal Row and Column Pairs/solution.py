class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowHash = Counter(tuple(row) for row in grid) 
        
        ans = 0
        for col in range(n):
            colArr = []
            for row in range(n):
                colArr.append(grid[row][col])
            
            colTuple = tuple(colArr)
            if colTuple in rowHash:
                ans += rowHash[colTuple]
        
        return ans