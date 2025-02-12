class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if (bitA | bitB) != bitC:
                if bitA == bitB == 1:
                    count += 2
                else:
                    count += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return count