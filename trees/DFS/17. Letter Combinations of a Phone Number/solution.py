class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        res = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            possibleLetters = letters[digits[index]]
            for char in possibleLetters:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res