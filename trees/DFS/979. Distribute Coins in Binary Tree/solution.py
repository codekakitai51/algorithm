# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(current):
            if current == None:
                return 0
            
            leftCoins = dfs(current.left)
            rightCoins = dfs(current.right)

            self.moves += abs(leftCoins) + abs(rightCoins)

            return (current.val - 1) + leftCoins + rightCoins
        
        dfs(root)

        return self.moves