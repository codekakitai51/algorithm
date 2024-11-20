class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

    # 32ビットの各ビットを調べる
        for i in range(32):  # iはビット位置 (0から31まで)
            bit_count = 0

            # 配列内のすべての数のiビット目をカウント
            for num in nums:
                bit_count += (num >> i) & 1

            # カウントが3で割り切れない場合、結果のiビット目をセット
            if bit_count % 3 != 0:
                # 符号ビットを考慮 (31番目のビットは負の数に影響)
                if i == 31:
                    result -= (1 << i)
                else:
                    result |= (1 << i)

        return result