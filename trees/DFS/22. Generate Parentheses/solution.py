class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(pattern, openP, closeP):
            if len(pattern) == 2 * n:
                ans.append(pattern)
                return

            if openP < n:
                backtrack(pattern + '(', openP + 1, closeP)
            if closeP < openP:
                backtrack(pattern + ')', openP, closeP + 1)

        backtrack("", 0, 0)
        return ans
