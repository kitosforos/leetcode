# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def aux(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            aux(root.left)
            aux(root.right)

        aux(root)
        return root