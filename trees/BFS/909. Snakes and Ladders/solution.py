class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque()
        q.append([1, 0]) # [square, moves]
        board.reverse()
        visit = set()

        def squareToPosi(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 == 1:
                c = n - 1 - c

            return r, c

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextsquare = square + i
                r, c = squareToPosi(nextsquare)
    
                if board[r][c] != -1:
                    nextsquare = board[r][c]
            
                if nextsquare == n ** 2:
                    return moves + 1

                if nextsquare not in visit:
                    visit.add(nextsquare)
                    q.append([nextsquare, moves + 1])
                
        return -1


