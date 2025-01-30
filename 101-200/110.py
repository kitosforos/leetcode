# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        
        def solve(root):
            if not root:
                return True
            
            return ((abs(dfs(root.left) - dfs(root.right)) <= 1) 
                and solve(root.left) and solve(root.right))
        
        return solve(root)