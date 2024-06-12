class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pre, cur, res = 0, 0, 0

        for i in range(len(rungs)):
            cur = rungs[i]
            res += (cur - pre - 1) // dist
            pre = cur
        
        return res

# cur - pre - 1 -> need to subtract 1 because the current rung is already there