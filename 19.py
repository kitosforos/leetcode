# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next

        if fast == None:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next
        else:
            head = None
        return head