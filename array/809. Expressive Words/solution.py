class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # hashMap can't use this problem because we need to memorize ORDER. hashMap does not gurantee the ORDER in general.
        def process(s):
            char, count = [s[0]], [1]
            for i in range(1, len(s)):
                if s[i] == char[-1]:
                    count[-1] += 1
                else:
                    char.append(s[i])
                    count.append(1)
            
            return char, count

        ans = 0
        # chr = ['a', 'b', 'c'], count = [1, 2, 3]
        sChr, sCount = process(s)

        for word in words:
            wChr, wCount = process(word)

            if wChr == sChr:
                counter = 0
                for i in range(len(sCount)):
                    if sCount[i] == wCount[i] or (sCount[i] > wCount[i] and sCount[i] >= 3):
                        counter += 1
                if counter == len(wChr):
                    ans += 1    
        
        return ans