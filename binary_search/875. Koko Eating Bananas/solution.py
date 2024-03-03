import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)

        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            time = 0

            for num in piles:
                time += math.ceil(num / k)
            
            if time <= h:
                r = k - 1
            else:
                l = k + 1
        
        return l