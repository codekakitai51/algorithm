# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def helperDFS(node):
            if not node:
                return False
            
            left = helperDFS(node.left)
            right = helperDFS(node.right)
            mid = node == p or node == q

            if left + mid + right >= 2:
                self.ans = node
            
            return left or mid or right

        helperDFS(root)
        return self.ans