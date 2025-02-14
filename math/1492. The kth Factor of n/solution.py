class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        smallF, largeF = [], []
        for f in range(1, int(n ** 0.5) + 1):
            if n % f == 0:
                smallF.append(f)
                if f != n // f:
                    largeF.append(n // f)
        
        factor = smallF + largeF[::-1]

        return factor[k - 1] if k <= len(factor) else -1

        # c = 0
        # for num in range(1, n + 1):
        #     if n % num == 0:
        #         c += 1
        #         if c == k:
        #             return num
        # return -1