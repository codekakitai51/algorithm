class TreeNode:
    def __init__(self, val, L, R):
        self.left = None
        self.right = None
        self.L = L
        self.R = R
        self.sum = val

class NumArray:

    def __init__(self, nums: List[int]):
        def makeTree(L, R):
            if L == R:
                return TreeNode(nums[L], L, R)
            
            M = (L + R) // 2
            root = TreeNode(0, L, R)
            root.left = makeTree(L, M)
            root.right = makeTree(M + 1, R)
            root.sum = root.left.sum + root.right.sum
            return root
        
        self.root = makeTree(0, len(nums) - 1)
        
    def update(self, index: int, val: int) -> None:
        def helperUpdate(root, idx, val):
            if root.L == root.R:
                root.sum = val
                return
            
            M = (root.L + root.R) // 2
            if idx <= M:
                helperUpdate(root.left, idx, val)
            else:
                helperUpdate(root.right, idx, val)
            
            root.sum = root.left.sum + root.right.sum
        
        helperUpdate(self.root, index, val)

    def sumRange(self, left, right):
        def helperSumRange(root, L, R):
            if root.L == L and root.R == R:
                return root.sum
            
            M = (root.L + root.R) // 2
            if R <= M:
                return helperSumRange(root.left, L, R)
            elif L > M:
                return helperSumRange(root.right, L, R)
            else:
                leftSum = helperSumRange(root.left, L, M)
                rightSum = helperSumRange(root.right, M+1, R)
                return leftSum + rightSum
        
        return helperSumRange(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)