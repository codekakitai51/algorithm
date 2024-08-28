# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {}
        for i, v in enumerate(inorder):
            inorderIdx[v] = i
        
        self.reversePostorderIdx = len(postorder) - 1

        def arrToTree(l, r):
            

            if l > r: return

            nodeVal = postorder[self.reversePostorderIdx]
            node = TreeNode(nodeVal)
            self.reversePostorderIdx -= 1

            node.right = arrToTree(inorderIdx[nodeVal] + 1, r)
            node.left = arrToTree(l, inorderIdx[nodeVal] - 1)

            return node

        return arrToTree(0, len(inorder) - 1)