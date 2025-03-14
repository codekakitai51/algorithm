class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = Counter(s)
        sortedChars = sorted(freq.keys(), key=lambda x: -freq[x])

        print(sortedChars)

        c = 0
        for i, char in enumerate(sortedChars):
            process = i // 9 + 1
            c += freq[char] * process
        
        return c