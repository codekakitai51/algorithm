class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leftStep = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= leftStep:
                leftStep = 1
            else:
                leftStep += 1
        
        return True if leftStep == 1 else False