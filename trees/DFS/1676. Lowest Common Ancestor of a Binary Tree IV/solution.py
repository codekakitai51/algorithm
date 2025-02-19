# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        seen = set(nodes)
        
        def dfs(node):
            if not node:
                return None
            
            if node in seen:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
            
            return None
        
        return dfs(root)