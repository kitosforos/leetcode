# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def aux(root):
            if not root:
                return 0
            res = 1
            resl = aux(root.left)
            resr = aux(root.right)
            res += max(resl, resr)
            return res
        
        return aux(root)