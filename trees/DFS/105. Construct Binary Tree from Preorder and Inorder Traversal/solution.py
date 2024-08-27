# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def arrToTree(l, r):
            nonlocal preIdx

            if l > r: return None

            node = TreeNode(preorder[preIdx])
            preIdx += 1

            node.left = arrToTree(l, inorderHash[node.val] - 1)
            node.right = arrToTree(inorderHash[node.val] + 1, r)
            
            return node


        inorderHash = {}
        for idx, val in enumerate(inorder):
            inorderHash[val] = idx
        
        preIdx = 0

        return arrToTree(0, len(inorder) - 1)