class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlti = 0
        curAlti = 0
        for alti in gain:
            curAlti += alti
            maxAlti = max(maxAlti, curAlti)
        
        return maxAlti