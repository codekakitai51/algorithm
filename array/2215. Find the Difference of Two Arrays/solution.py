class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[], []]
        nums1 = set(nums1)
        nums2 = set(nums2)

        for num1 in nums1:
            if num1 not in nums2:
                ans[0].append(num1)
        
        for num2 in nums2:
            if num2 not in nums1:
                ans[1].append(num2)
    
        return ans