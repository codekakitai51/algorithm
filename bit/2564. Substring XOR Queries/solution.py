class Solution:
    def substringXorQueries(self, s, queries):
        # cant understand this
        n = len(s)
        seen = defaultdict(lambda: [-1, -1])
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                seen[0] = [i, i]
                continue
            v = 0
            for j in range(i, n):
                v = v * 2 + int(s[j])
                if v > 2 ** 32: break
                seen[v] = [i, j]
        return [seen[sec ^ fir] for fir, sec in queries]
        
# this is too late O(n * q) 
    # def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
    #     # because it's EOR, val ^ first == second -> val == first ^ second
    #     res = []

    #     for first, second in queries:
    #         val = bin(first ^ second)[2:]

    #         i = s.find(val)
    #         res.append([-1, -1]) if i < 0 else res.append([i, i + len(val) - 1])
    #         # num: 0 is False, others are True
    #     return res
