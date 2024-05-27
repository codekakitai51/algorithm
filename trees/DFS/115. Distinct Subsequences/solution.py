class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # memoization T:O(len(t) * len(s))
        cache = [[-1] * len(t) for _ in range(len(s))]

        def memoDFS(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            if s[i] == t[j]:
                cache[i][j] = memoDFS(i + 1, j + 1) + memoDFS(i + 1, j)
            else:
                cache[i][j] = memoDFS(i + 1, j)

            return cache[i][j]
        
        return memoDFS(0, 0)
