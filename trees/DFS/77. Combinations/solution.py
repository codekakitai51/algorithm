class Solution:
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


# brute force time -> O(2 ** n * k)

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