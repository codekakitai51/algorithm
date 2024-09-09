class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        firstCol = False

        for r in range(0, R):
            if matrix[r][0] == 0:
                firstCol = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
            
        for r in range(1, R):
            for c in range(1, C):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(1, C):
                matrix[0][c] = 0
            
        if firstCol:
            for r in range(R):
                matrix[r][0] = 0


        # for r in range(R):
        #     for c in range(C):
        #         if matrix[r][c] == 0:
        #             matrix[r][c] = None
        
        # for r in range(R):
        #     for c in range(C):
        #         if matrix[r][c] == None:
        #             matrix[r][c] = 0
        #             # to right boundary
        #             newC = 0
        #             while newC < C:
        #                 if matrix[r][newC] != None:
        #                     matrix[r][newC] = 0
        #                 newC += 1

        #             # to bottom boundary
        #             newR = 0
        #             while newR < R:
        #                 if matrix[newR][c] != None:
        #                     matrix[newR][c] = 0
        #                 newR += 1
                    
        
        