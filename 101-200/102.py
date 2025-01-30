# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []

        change = True
        while change == True:
            change = False
            aux = []
            while q:
                node = q.popleft()
                if node:
                    aux.append(node)
                change = True
            if aux:
                res.append(aux)
            for i in range(len(aux)):
                q.append(aux[i].left)
                q.append(aux[i].right)
        return [[node.val for node in sublist] for sublist in res]
            