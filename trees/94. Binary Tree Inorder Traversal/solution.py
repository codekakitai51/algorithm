# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # --- recursive
    #     result = []

    #     def _inorder(node):
    #         if not node: return

    #         _inorder(node.left)
    #         result.append(node.val)
    #         _inorder(node.right)

    #     _inorder(root)
    #     return result

    # --- iteratively
        # with using Stack, it's almost the same as recursive (call stack)
        res, stack = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res