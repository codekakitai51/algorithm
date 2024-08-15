class Solution:
    def isPalindrome(self, x: int) -> bool:
# without substring idea: divide hilf and compare
        # return False if the num ends with 0 otherwise error
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        
        return x == reversedNum or x == reversedNum // 10



        # if x < 0:
        #     return False

        # reversedX = int(str(x)[::-1])
        # if x == reversedX:
        #     return True
        # return False

