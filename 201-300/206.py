# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        current = head
        prev = None

        while current:
            nextCurrent = current.next
            current.next = prev
            prev = current
            current = nextCurrent
        
        return prev
        