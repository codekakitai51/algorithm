class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def rec(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s1) and j == len(s2):
                return True
            
            ans = False

            if i < len(s1) and s1[i] == s3[i + j]:
                ans |= rec(i + 1, j)
            
            if j < len(s2) and s2[j] == s3[i + j]:
                ans |= rec(i, j + 1)
            
            memo[(i, j)] = ans

            return ans
        
        return rec(0, 0)
            

            

