# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tiltSum = 0

        def DFS(node):
            if not node:
                return 0

            left = DFS(node.left)
            right = DFS(node.right)
            
            self.tiltSum += abs(left - right)

            return node.val + left + right

        DFS(root)

        return self.tiltSum