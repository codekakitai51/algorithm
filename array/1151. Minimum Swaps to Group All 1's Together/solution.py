class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneL = 0
        for n in data:
            if n == 1:
                oneL += 1
                
        if oneL <= 1:
            return 0
        
        l = 0
        zeroC = 0
        res = float("inf")
        for r in range(len(data)):
            if data[r] == 0:
                zeroC += 1   
            
            if r - l + 1 == oneL:
                res = min(res, zeroC)

                if data[l] == 0:
                    zeroC -= 1
                l += 1
        
        return res

