from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")
        
        for num in nums:
            if num <= first_min:
                first_min = num  # Update the smallest number
            elif num <= second_min:
                second_min = num  # Update the second smallest number
            else:
                return True  # Found a valid increasing triplet
        
        return False
