# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        t = start
        p = end
        
        for i in range(start, end):
            if pairs[i].key < pairs[p].key:
                pairs[i], pairs[t] = pairs[t], pairs[i]
                t += 1
        
        if pairs[p].key <= pairs[t].key:
            pairs[p], pairs[t] = pairs[t], pairs[p]

        self.quickSortHelper(pairs, start, t-1)
        self.quickSortHelper(pairs, t+1, end)

        return pairs


# tips: use INDEX not SLICE(cz slice makes a copy so recursion does not change original array) when implementing in-place quick sort