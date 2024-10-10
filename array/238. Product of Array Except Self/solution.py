class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        leftProduct = 1
        for i in range(len(nums)):
            ans[i] = leftProduct
            leftProduct *= nums[i]
        
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= rightProduct
            rightProduct *= nums[i]
        
        return ans



# not allowed to use division!!!
        # productSum = 0
        # zeroCount = 0

        # # count 0 and product all nums
        # for num in nums:
        #     if num == 0:
        #         zeroCount += 1
        #         if zeroCount >= 2:
        #             return [0] * len(nums)
        #     else:
        #         if productSum == 0:
        #             productSum = num
        #         else:
        #             productSum *= num
        
        # # make each num and put it in ans
        # ans = []
        # if zeroCount == 1:
        #     for num in nums:
        #         if num == 0:
        #             ans.append(productSum)
        #         else:
        #             ans.append(0)       
        # else:
        #     for num in nums:
        #         ans.append(productSum // num)

        # return ans        
