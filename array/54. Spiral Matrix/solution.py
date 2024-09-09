class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    # set up boundary -> T:O(n), S:O(1)
        R, C = len(matrix), len(matrix[0])
        left, up = 0, 0
        right = C - 1
        bottom = R - 1
        res = []

        while len(res) < R * C:

            for col in range(left, right + 1):
                res.append(matrix[up][col])

            for row in range(up + 1, bottom + 1):
                res.append(matrix[row][right])

            if up != bottom:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
            
            if left != right:
                for row in range(bottom - 1, up, -1):
                    res.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            bottom -= 1
        
        return res
        