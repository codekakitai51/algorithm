# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, stack, targetSum):
            if not root: return False
            stack.append(root.val)

            if not root.left and not root.right and sum(stack) == targetSum:
                return True
            
            if helper(root.left, stack, targetSum):
                return True
            
            if helper(root.right, stack, targetSum):
                return True

            stack.pop()
            return False

        stack = []
        return helper(root, stack, targetSum)
    
# better to use curSum than stack to save space!