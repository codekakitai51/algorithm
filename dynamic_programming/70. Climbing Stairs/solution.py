class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        one, two = 1, 1 # tips: start from the top
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

        # memoization
        # def cacheDFS(n, cache):
        #     if n <= 2:
        #         return n
        #     if n in cache:
        #         return cache[n]

        #     cache[n] = cacheDFS(n-1, cache) + cacheDFS(n-2, cache)
        #     return cache[n]

        # return cacheDFS(n, {})