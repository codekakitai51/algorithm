class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numArr = []

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap[val] = len(self.numArr)
            self.numArr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            lastNum, idx = self.numArr[-1], self.hashMap[val]
            self.numArr[idx] = lastNum
            self.hashMap[lastNum] = idx

            # switch order in hashMap and numArr
            del self.hashMap[val]
            self.numArr.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        ranNum = random.randint(0, len(self.numArr) - 1)
        return self.numArr[ranNum]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()