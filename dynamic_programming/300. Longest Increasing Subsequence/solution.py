class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = 1
        subArr = [nums[0]] # subArr is always sorted

        def BS(arr, targetNum):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                if targetNum <= arr[mid]:
                    r = mid
                else:
                    l = mid + 1
                
            return l

        for num in nums[1:]:
            if subArr[-1] < num:
                subArr.append(num)
            else:
                # find num <=, and remove all using binary search library
                # targetIdx = bisect.bisect_left(subArr, num)
                targetIdx = BS(subArr, num)
                subArr[targetIdx] = num
        
        return len(subArr)