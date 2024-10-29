class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rowBox = ['' for _ in range(numRows)]
        currentRow = 0
        goingDown = False

        for letter in s:
            rowBox[currentRow] += letter

            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown
            
            currentRow += 1 if goingDown else -1
        
        res = ''
        for row in rowBox:
            res += ''.join(row)
        
        return res

