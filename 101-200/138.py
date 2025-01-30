"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        conex = {None : None}

        cur = head

        while cur:
            copy = ListNode(cur.val)
            conex[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = conex[cur]
            copy.next = conex[cur.next]
            copy.random = conex[cur.random]
            cur = cur.next
        
        return conex[head]