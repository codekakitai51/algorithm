# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:           
            q = deque()
            q.append(root)
            while len(q) > 0:
                box = []
                for _ in range(len(q)):
                    cur = q.popleft()
                    box.append(cur.val)
                    if cur.left: q.append(cur.left)
                    if cur.right: q.append(cur.right)
                res.append(box)
        return res
    