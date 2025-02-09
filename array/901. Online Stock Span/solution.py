class StockSpanner:

    def __init__(self):
        self.pStack = []
        # self.tempStack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.pStack and price >= self.pStack[-1][0]:
            ans += self.pStack.pop()[1]
        
        self.pStack.append((price, ans))
        return ans

# too slow and tempStack not needed
        # if not self.pStack or price < self.pStack[-1]:
        #     self.pStack.append(price)
        #     return 1
        
        # self.tempStack.append(price)
        # c = 1
        # while self.pStack and price >= self.pStack[-1]:
        #     self.tempStack.append(self.pStack.pop())
        #     c += 1
        
        # while self.tempStack:
        #     self.pStack.append(self.tempStack.pop())
        
        # return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)