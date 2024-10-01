class Solution:
    def reverseWords(self, s: str) -> str:
# since Python str data is immutable, solutiou is ... t, s -> O(n)
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                word = ''
                while i < len(s) and s[i] != ' ':
                    word += s[i]
                    i += 1
                stack.append(word)
            i += 1
        
        res = ''
        while stack:
            curWord = stack.pop()
            if res:
                res = res + ' ' + curWord
            else:
                res += curWord
        
        return res
