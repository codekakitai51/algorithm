class Solution:
    def compress(self, chars: List[str]) -> int:
        L = len(chars)
        l, write = 0, 0

        for r in range(L):
            if r == L - 1 or chars[r] != chars[r + 1]:
                chars[write] = chars[l]
                write += 1

                size = r - l + 1
                if size > 1:
                    for c in str(size):
                        chars[write] = c
                        write += 1
                l = r + 1
        
        return write