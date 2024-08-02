class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxDigit = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                maxDigit = max(maxDigit, num[i:i + 3])
        
        return maxDigit
        # this case, target is the same length so we can compare as string


# another solution
        # target = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        # intArr = []
        # for s in range(len(num) - 2):
        #     if num[s:s + 3] in target:
        #         intArr.append(int(num[s:s + 3]))
        
        # if not intArr:
        #     return "" 
        
        # else:
        #     maxVal = max(intArr)
        #     if maxVal == 0:
        #         return "000"
        #     else:
        #         return str(maxVal)
