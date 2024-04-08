class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if ord("0") <= ord(char) <= ord("9") 
                                       or ord("a") <= ord(char) <= ord("z"))

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        