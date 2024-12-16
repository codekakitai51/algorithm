# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curLevel, maxLevel = 1, 1
        maxLevelSum = float("-inf")
        q = deque([root])

        while q:
            curLevelSum = 0
            for _ in range(len(q)):
                curNode = q.popleft()
                curLevelSum += curNode.val

                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)

            if curLevelSum > maxLevelSum:
                maxLevelSum = curLevelSum
                maxLevel = curLevel
            
            curLevel += 1
        
        return maxLevel