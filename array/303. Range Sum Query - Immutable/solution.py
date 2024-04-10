class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        curSum = 0
        for n in nums:
            curSum += n
            self.prefixSum.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        L = self.prefixSum[left - 1] if left > 0 else 0
        R = self.prefixSum[right]
        return R - L


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)