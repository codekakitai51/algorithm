# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGoodNodes = 0
        maxVal = float("-inf")

        def DFS(node, maxVal):
            nonlocal numGoodNodes

            if not node: return
            if node.val >= maxVal:
                numGoodNodes += 1
                maxVal = node.val
            
            DFS(node.left, maxVal)
            DFS(node.right, maxVal)

        DFS(root, maxVal)
        return numGoodNodes