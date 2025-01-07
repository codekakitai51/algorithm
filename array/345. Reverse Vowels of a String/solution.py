class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        listS = list(s)  # 文字列をリストに変換

        l, r = 0, len(listS) - 1
        while l < r:
            # 左側が母音でない場合、次に進む
            while l < r and listS[l] not in vowels:
                l += 1
            # 右側が母音でない場合、前に戻る
            while l < r and listS[r] not in vowels:
                r -= 1

            # 両方が母音の場合、スワップする
            if l < r:
                listS[l], listS[r] = listS[r], listS[l]
                l += 1
                r -= 1

        return ''.join(listS)  # リストを再び文字列に変換
