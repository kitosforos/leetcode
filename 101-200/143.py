# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            tmpSecond = second.next
            second.next = prev
            prev = second
            second = tmpSecond
        
        first, second = head, prev

        while second:
            tmpF, tmpS = first.next, second.next
            first.next = second
            second.next = tmpF
            first, second = tmpF, tmpS
        