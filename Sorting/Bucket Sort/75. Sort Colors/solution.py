class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]
        for num in nums:
            bucket[num] += 1

        idx = 0
        for j in range(len(bucket)):
            for _ in range(bucket[j]):
                nums[idx] = j
                idx += 1

# tips: buket sort only can be used when the range of the input is known, merge sort is more general.