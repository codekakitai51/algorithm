class Solution:
    def isHappy(self, n: int) -> bool:
    # Floyd's Cycle-Finding Algorithm
        def getNext(n):
            sumNum = 0
            while n > 0:
                n, digit = n // 10, n % 10
                sumNum += digit ** 2
            
            return sumNum

        slow, fast = n, getNext(n)

        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        
        return fast == 1


        # sumSet = set()
        # curSum = n
        # while curSum not in sumSet:
        #     sumSet.add(curSum)
        #     tempSum = 0

        #     while curSum > 0:
        #         digit = curSum % 10
        #         curSum //= 10

        #         tempSum += digit ** 2

        #     if tempSum == 1:
        #         return True

        #     curSum = tempSum
        
        # return False
