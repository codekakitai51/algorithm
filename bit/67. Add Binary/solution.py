class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print(x, y)
        return bin(x)[2:]


        # a, b = int(a, 2), int(b, 2)
        # return bin(a + b)[2:]