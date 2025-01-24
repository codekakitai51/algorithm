class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = len(temperatures)
        ans = [0] * L
        stack = []

        for curIdx, curTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curTemp:
                prevIdx = stack.pop()
                ans[prevIdx] = curIdx - prevIdx
            stack.append(curIdx)
        
        return ans


# O(n ^ 2)        
        # ans = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             ans[i] = j - i
        #             break
        
        # return ans