class Solution:
    def intToRoman(self, num: int) -> str:
        romanNum = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        res = ""

        for value in sorted(romanNum.keys(), reverse=True):
            while num >= value: 
                res += romanNum[value] 
                num -= value 

        return res

        # The approach needed is to select the largest possible value from the keys in the dictionary and subtract that value from the original number.
        # O(1)
