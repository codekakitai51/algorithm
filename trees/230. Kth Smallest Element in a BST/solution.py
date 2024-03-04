# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = None
        self.inorderTraversal(root, k)
        return self.result
    
    def inorderTraversal(self, node, k):
        if not node or self.count >= k: 
# why self.count >= k is required? -> 例えば、k 番目の要素を左の子ノードで見つけた後、その関数の実行は return で終了しますが、
# その親ノードに戻ったときにまだ右の子を探索する必要があるかのように振る舞います。これは、各再帰呼び出しが独立していて、return が他の呼び出しに伝播されないためです。
            return
        
        self.inorderTraversal(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        
        self.inorderTraversal(node.right, k)