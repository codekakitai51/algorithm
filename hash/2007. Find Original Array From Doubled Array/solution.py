class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        freq = {}
        for num in changed:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        original = []
        for num in changed:
            if freq[num] == 0:
                continue
            if num * 2 in freq and freq[num * 2] > 0:
                original.append(num)
                freq[num] -= 1
                freq[num * 2] -= 1
            else:
                return []

        return original


# too slow ↓

        # L = len(changed)
        # res = []

        # if L % 2 == 1:
        #     return res

        # changed.sort()
        # used = [False] * L

        # for i in range(L):
        #     if used[i]:
        #         continue

        #     found = False
        #     for j in range(i + 1, L):
        #         if not used[j] and changed[j] == 2 * changed[i]:
        #             res.append(changed[i])
        #             used[j] = True
        #             found = True
        #             break
            
        #     if not found:
        #         return []

        # return res