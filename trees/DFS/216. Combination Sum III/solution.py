class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def BT(remain, comb, nextStart):
            if remain == 0 and len(comb) == k:
                res.append(comb[:])
                return

            elif remain < 0 or len(comb) == k:
                return
            
            for num in range(nextStart, 9):
                nextNum = num + 1
                comb.append(nextNum)
                BT(remain - nextNum, comb, nextNum)
                comb.pop()

        BT(n, [], 0)
        return res