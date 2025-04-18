class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        c = 0
        while l < r:
            if s[l] != s[r]:
                c += 1
            l += 1
            r -= 1

            if c > 2:
                return False
        
        return True