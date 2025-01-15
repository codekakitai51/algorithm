from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        valSeen = defaultdict(int)  # 累積和を記録する辞書
        valSeen[0] = 1  # 初期値として空のパスを追加
        count = 0  # パスの数を記録する変数

        def preOrder(node, curSum):
            nonlocal count

            if not node:
                return
            
            # 現在の累積和を計算
            curSum += node.val
            
            # 目標値との差が辞書に存在するか確認
            count += valSeen[curSum - targetSum]
            
            # 現在の累積和を辞書に追加
            valSeen[curSum] += 1
            
            # 左右の子ノードを再帰的に探索
            preOrder(node.left, curSum)
            preOrder(node.right, curSum)
            
            # バックトラック：現在の累積和を辞書から削除
            valSeen[curSum] -= 1
        
        # ルートノードから探索を開始
        preOrder(root, 0)

        return count
