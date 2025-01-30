"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        otn = {}

        def dfs(cur):
            if cur in otn:
                return otn[cur]
            
            copy = Node(cur.val)
            otn[cur] = copy
            for ne in cur.neighbors:
                copy.neighbors.append(dfs(ne))
            return copy

        return dfs(node) if node else None

        