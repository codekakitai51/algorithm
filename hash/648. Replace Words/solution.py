class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        stArr = sentence.split()
        dictSet = set(dictionary) # key point is to use set to speed up the search. Search in set is O(1) while in list is O(n).

        def shortestRoot(word, dictSet):
            for j in range(len(word)):
                curWord = word[0:j + 1]
                if curWord in dictSet:
                    return curWord
            
            return word

        for i in range(len(stArr)):
            stArr[i] = shortestRoot(stArr[i], dictSet)
        
        return " ".join(stArr)
    
# T: O(d * w + s * w^2) Let d be the number of words in the dictionary, s be the number of words in the sentence, and w be the average length of each word.
# S: O(d * w + s * w) 
        