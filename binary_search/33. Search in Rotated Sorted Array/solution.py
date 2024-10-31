from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ピボットインデックスを見つける
        l, r = -1, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m
            else:
                r = m
        pivotIdx = r

        # 汎用バイナリサーチ関数の定義（めぐる式）
        def BS(nums, left_boundary, right_boundary):
            l, r = left_boundary - 1, right_boundary + 1
            while r - l > 1:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m
            # rが範囲内かつnums[r]がtargetである場合のみインデックスを返す
            return r if r < len(nums) and nums[r] == target else -1

        # ピボットの左側で探索
        if (ans := BS(nums, 0, pivotIdx - 1)) != -1:
            return ans

        # ピボットの右側で探索
        return BS(nums, pivotIdx, len(nums) - 1)
