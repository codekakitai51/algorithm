class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1

        if not top <= bot: return False
        
        tarArr = matrix[row]
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if tarArr[m] == target:
                return True
            elif tarArr[m] > target:
                r = m - 1
            elif tarArr[m] < target:
                l = m + 1
        
        return False
