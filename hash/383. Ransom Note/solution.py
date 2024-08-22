class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False
        
        rHash, mHash = {}, {}
        for char in ransomNote:
            if char not in rHash:
                rHash[char] = 1
            else:
                rHash[char] += 1
        
        for char in magazine:
            if char not in mHash:
                mHash[char] = 1
            else:
                mHash[char] += 1
        
        for k, v in rHash.items():
            if k in mHash:
                if v > mHash[k]:
                    return False

            else:
                return False
        
        return True
