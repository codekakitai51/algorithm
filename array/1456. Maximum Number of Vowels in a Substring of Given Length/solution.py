class Solution:
    def maxVowels(self, s: str, k: int) -> int:
# This is smarter
        vowels = {'a', 'e', 'i', 'o', 'u'}
        c = 0
        
        # 最初のウィンドウの母音のカウント
        for i in range(k):
            if s[i] in vowels:
                c += 1
        
        maxC = c

        # スライドウィンドウの実装
        for i in range(k, len(s)):
            # 左端を取り除く
            if s[i - k] in vowels:
                c -= 1
            
            # 右端を追加する
            if s[i] in vowels:
                c += 1
            
            # 最大値を更新
            maxC = max(maxC, c)
        
        return maxC

        # q = deque()
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # c = 0

        # for i in range(k):
        #     if s[i] in vowels:
        #         c += 1
        #     q.append(s[i])
        # maxC = c
        
        # for i in range(k, len(s)):
        #     sRemoved = q.popleft()
        #     if sRemoved in vowels:
        #         c -= 1
            
        #     sNew = s[i]
        #     q.append(sNew)
        #     if sNew in vowels:
        #         c += 1
            
        #     maxC = max(maxC, c)
        
        # return maxC