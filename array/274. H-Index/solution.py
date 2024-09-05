class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        numOfCitations = len(citations)
        for i in range(len(citations)):
            if numOfCitations <= citations[i]:
                return numOfCitations
            numOfCitations -= 1
        
        return 0