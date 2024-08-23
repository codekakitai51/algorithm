class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        L = len(s)
        sHash, tHash = {}, {}
        sCount, tCount = 0, 0

        for i in range(L):
            if s[i] not in sHash:
                sHash[s[i]] = sCount
                sCount += 1
            
            if t[i] not in tHash:
                tHash[t[i]] = tCount
                tCount += 1
            
        sArr, tArr = [], []
        for i in range(L):
            sArr.append(sHash[s[i]])
            tArr.append(tHash[t[i]])
        
        return True if sArr == tArr else False

