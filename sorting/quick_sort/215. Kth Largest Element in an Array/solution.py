class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

# quickSelect -> T: O(n) on average but T: O(n^2) in worst case
        def quickSelect(s, e):
            pivot = e
            left = s

            for i in range(s, e):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1 

            nums[left], nums[pivot] = nums[pivot], nums[left]

            if k < left:     return quickSelect(s, left - 1)
            elif left < k:   return quickSelect(left + 1, e)
            else:                       return nums[left]
        
        return quickSelect(0, len(nums) - 1)

# quickSort -> T: O(nlogn) on average but T: O(n^2) in worst case
        # def quickSort(s, e):
        #     if (e - s) + 1 <= 1: return

        #     pivot = e
        #     left = s

        #     for i in range(s, e):
        #         if nums[i] <= nums[pivot]:
        #             nums[i], nums[left] = nums[left], nums[i]
        #             left += 1
            
        #     nums[left], nums[pivot] = nums[pivot], nums[left]

        #     quickSort(s, left - 1)
        #     quickSort(left + 1, e)

        #     return
        
        # quickSort(0, len(nums) - 1)

        # return nums[k]