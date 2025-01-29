# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_left(root, dummy):
            if not dummy:
                return True
            if dummy and dummy.val >= root.val:
                return False
            return dfs_left(root, dummy.left) and dfs_left(root, dummy.right)
        
        def dfs_right(root, dummy):
            if not dummy:
                return True
            if dummy and dummy.val <= root.val:
                return False
            return dfs_right(root, dummy.left) and dfs_right(root, dummy.right)
        
        def dfs(root):
            return dfs_left(root, root.left) and dfs_right(root, root.right)
        
        def solve(root):
            if not root:
                return True
            return dfs(root) and solve(root.right) and solve(root.left)
            
        return solve(root)