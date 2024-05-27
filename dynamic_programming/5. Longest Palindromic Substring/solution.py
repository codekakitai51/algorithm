class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def helper(l, r):
            nonlocal res, resLen  # 外部スコープの変数を使用することを宣言
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i, i)
        
            helper(i, i + 1)

        return res
