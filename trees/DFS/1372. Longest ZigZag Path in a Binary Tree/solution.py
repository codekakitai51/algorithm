from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def zigZagDFS(node, prevDirFlag, pathCount): # prevDirFlag = True -> right False -> left
            nonlocal ans

            if not node:
                ans = max(ans, pathCount - 1)
                return

            if prevDirFlag:  # 直前が「右」なら左へ
                zigZagDFS(node.left, False, pathCount + 1)  # ZigZag 継続
                zigZagDFS(node.right, True, 1)  # 新しい ZigZag パス開始
            else:  # 直前が「左」なら右へ
                zigZagDFS(node.right, True, pathCount + 1)  # ZigZag 継続
                zigZagDFS(node.left, False, 1)  # 新しい ZigZag パス開始

        # root から左・右の2方向で ZigZag を開始
        zigZagDFS(root, True, 0)  # 左方向から開始

        return ans
