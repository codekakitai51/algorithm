class SmallestInfiniteSet:

    def __init__(self):
        self.exists = [True] * 1001 # for index convinient
        self.minHeap = list(range(1, 1001))
        heapq.heapify(self.minHeap)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.minHeap)
        self.exists[smallest] = False
        return smallest

    def addBack(self, num: int) -> None:
        if not self.exists[num]:
            heapq.heappush(self.minHeap, num)
            self.exists[num] = True
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)