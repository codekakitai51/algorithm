class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search 「めぐる式」
        def isOk(curPowNum):
            return curPowNum > x

        ng, ok = -1, x + 1

        while ok - ng > 1:
            mid = (ng + ok) // 2
            curPowNum = mid ** 2

            if curPowNum == x:
                return mid

            if isOk(curPowNum):
                ok = mid
            else:
                ng = mid

        return ng


        # binary search
        # if x == 0 or x == 1:
        #     return x
        # l, r = 0, x
        # while l <= r:
        #     m = (l + r) // 2
        #     curNum = m ** 2

        #     if curNum < x:
        #         l = m + 1
        #     elif curNum > x:
        #         r = m - 1
        #     else:
        #         return m
        
        # return r
        
        # if x == 0 or x == 1:
        #     return x

        # for root in range(1, x + 1):
        #     if root ** 2 == x:
        #         return root
        #     elif root ** 2 > x:
        #         return root - 1
