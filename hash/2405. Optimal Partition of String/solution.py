class Solution:
    def partitionString(self, s: str) -> int:
        seen = [-1] * 26
        subStart = 0
        c = 1

        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')] >= subStart:
                c += 1
                subStart = i
            seen[ord(s[i]) - ord('a')] = i
        
        return c

# set()
        # chaSet = set()
        # c = 0
        # for cha in s:
        #     if cha in chaSet:
        #         chaSet = set()
        #         chaSet.add(cha)
        #         c += 1
        #     else:
        #         chaSet.add(cha)
        # c += 1 # for the last substring
        # return c
