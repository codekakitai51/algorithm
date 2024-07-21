class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # The champion should be stronger than all the other teams.
        # Champion's result should be sum(champion's result) == len(grid) - 1
        for team in range(len(grid)):
            if sum(grid[team]) == len(grid) - 1:
                return team


        # hashMap = {}
        # for team in range(len(grid)):
        #     for result in grid[team]:
        #         if result == 1:
        #             if team not in hashMap:
        #                 hashMap[team] = 1
        #             else:
        #                 hashMap[team] += 1
        
        # return max(hashMap, key=hashMap.get)
