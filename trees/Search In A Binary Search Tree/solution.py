# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        if not node: return 

        if node.val > val:
            return self.searchBST(node.left, val)
        
        elif node.val < val:
            return self.searchBST(node.right, val)
        
        else:
            return node