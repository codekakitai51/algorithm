class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashSet = set(nums)

        for num in hashSet:
            if not num - 1 in hashSet:
                curNum = num
                streak = 0

                while curNum in hashSet:
                    streak += 1
                    curNum += 1
            
                res = max(res, streak)
        
        return res