class Solution:
# time -> O(k * C(n, k)) Combinations of n choose k
#  why k * -> because we are copying the current combination to the result list
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res


# brute force time -> O(k * 2^n)

        # num = 1
        # res = []

        # def helper(n, k, num, curSets, res):
        #     if len(curSets) >= k:
        #         res.append(curSets.copy())
        #         return
            
        #     if num > n:
        #         return
            
        #     curSets.append(num)
        #     helper(n, k, num + 1, curSets, res)
        #     curSets.pop()
        #     helper(n, k, num + 1, curSets, res)

        #     return
        
        # helper(n, k, num, [], res)
        # return res