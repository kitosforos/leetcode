# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        l = root.left
        r = root.right
        return self.helper(l, r)

    def helper(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        return False
        