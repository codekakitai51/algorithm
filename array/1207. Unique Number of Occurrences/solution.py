class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        hashSet = set()
        for val in hashMap.values():
            hashSet.add(val)
        
        return len(hashMap) == len(hashSet)