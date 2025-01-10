class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
# using Counter library
        if len(word1) != len(word2):
            return False
        
        word1_map = Counter(word1)
        word2_map = Counter(word2)

        if set(word1_map) != set(word2_map):
            return False

        return True if sorted(word1_map.values()) == sorted(word2_map.values()) else False

        # if len(word1) != len(word2):
        #     return False
        # L = len(word1)

        # wordCount1, wordCount2 = {}, {}
        # for i in range(L):
        #     if word1[i] in wordCount1:
        #         wordCount1[word1[i]] += 1
        #     else:
        #         wordCount1[word1[i]] = 1

        #     if word2[i] in wordCount2:
        #         wordCount2[word2[i]] += 1
        #     else:
        #         wordCount2[word2[i]] = 1

        # sortedKeys1 = wordCount1.keys()
        # sortedKeys2 = wordCount2.keys()
        # sortedValue1 = sorted(wordCount1.values())
        # sortedValue2 = sorted(wordCount2.values())

        # return True if (sortedKeys1 == sortedKeys2) and (sortedValue1 == sortedValue2) else False