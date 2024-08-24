class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sArr = s.split()
        if len(pattern) != len(sArr):
            return False
        
        pToS, sToP = {}, {}
        for c, w in zip(pattern, sArr):
            if c not in pToS:
                if w in sToP:
                    return False
                else:
                    pToS[c] = w
                    sToP[w] = c
            else:
                if pToS[c] != w:
                    return False        
        
        return True