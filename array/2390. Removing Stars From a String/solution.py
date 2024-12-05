class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for cha in s:
            if cha == '*':
                stack.pop()
            else:
                stack.append(cha)
        
        ans = ""
        for cha in stack:
            ans += cha
        
        return ans