# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # count = 1 + left + right

        def DFS(node):
            if node == None:
                return 0
            
            return 1 + DFS(node.left) + DFS(node.right)
        
        return DFS(root)

