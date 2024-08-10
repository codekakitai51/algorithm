# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prevVal = None

        def helperDFS(cur):
            nonlocal res, prevVal
            if not cur:
                return
            
            helperDFS(cur.left)
            
            if prevVal != None:
                res = min(res, abs(prevVal - cur.val))

            prevVal = cur.val

            helperDFS(cur.right)

            return res
        
        helperDFS(root)

        return res