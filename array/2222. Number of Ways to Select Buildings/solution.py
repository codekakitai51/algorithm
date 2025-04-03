class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        zero, one, oneZero, zeroOne = 0, 0, 0, 0
        for c in s:
            if c == '0':
                zero += 1
                oneZero += one
                ways += zeroOne
            else:
                one += 1
                zeroOne += zero
                ways += oneZero
        
        return ways
                
# make big problems small first, and then solve the small problems