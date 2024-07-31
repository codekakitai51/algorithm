class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        vows = ('a', 'e', 'i', 'o', 'u')

        for i in range(len(s)):
            vC, cC = 0, 0
            for j in range(i, len(s)):
                if s[j] in vows:
                    vC += 1
                else:
                    cC += 1
                
                if vC == cC and (vC * cC) % k == 0:
                    res += 1
        
        return res