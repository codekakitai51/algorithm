class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# this is better O(n), O(1)
        l, r = 0, len(numbers) - 1
        while l < r:
            numSum = numbers[l] + numbers[r]

            if numSum == target:
                return [l + 1, r + 1]
            elif numSum < target:
                l += 1
            
            elif numSum > target:
                r -= 1

        return [-1, -1]

# O(nlogn), O(1)
        # def binarySearch(l, r):
        #     while l <= r:
        #         m = (l + r) // 2
        #         if numbers[m] < curTarget:
        #             l = m + 1
        #         elif numbers[m] > curTarget:
        #             r = m - 1
        #         else:
        #             return m
        #     return 0

        # for i in range(len(numbers)):
        #     curTarget = target - numbers[i]
        #     l, r = i + 1, len(numbers) - 1

        #     secondIdx = binarySearch(l, r)
        #     if secondIdx:
        #         break
        
        # return [i + 1, secondIdx + 1]
        