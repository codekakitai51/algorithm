class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        m = len(potions)

        for s in spells:
            target = math.ceil(success / s)
            targetIdx = bisect.bisect_left(potions, target)
            numPro = m - targetIdx
            res.append(numPro)
        
        return res

# time limit exceed O(n * m)
        # res = []
        # for s in spells:
        #     c = 0
        #     for p in potions:
        #         if s * p >= success:
        #             c += 1
            
        #     res.append(c)
        
        # return res