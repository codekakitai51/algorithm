class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isGCD(i):
            if len(str1) % i or len(str2) % i:
                return False
            
            n1 = len(str1) // i
            n2 = len(str2) // i
            base = str1[:i]

            return True if base * n1 == str1 and base * n2 == str2 else False
            

        for i in range(min(len(str1), len(str2)), 0, -1):
            if isGCD(i):
                return str1[:i]
        
        return ""