class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        curEnd, curFar = 0, 0

        for i in range(len(nums) - 1):
            curFar = max(curFar, i + nums[i])

            if i == curEnd:
                ans += 1
                curEnd = curFar
        
        return ans
    