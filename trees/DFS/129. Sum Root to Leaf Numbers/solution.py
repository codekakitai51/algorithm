# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def helperDFS(node, curNum):
            nonlocal total
            if not node:
                return
            
            curNum = curNum * 10 + node.val

            if not (node.left or node.right):
                total += curNum
            
            helperDFS(node.left, curNum)
            helperDFS(node.right, curNum)
        
        helperDFS(root, 0)
        return total

        # stack, sumsArr = [], []
        
        # def helperDFS(node):
        #     nonlocal stack, sumsArr

        #     if not node:
        #         return 
            
        #     stack.append(node.val)

        #     if not node.left and not node.right:
        #         num = int("".join(map(str, stack)))
        #         sumsArr.append(num)

        #     helperDFS(node.left)    
        #     helperDFS(node.right)
        #     stack.pop()            
        
        # helperDFS(root)

        return sum(sumsArr)
