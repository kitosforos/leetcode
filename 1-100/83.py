# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        if current is not None and current.next is not None:
            point = current.next
        else:
            return head
        while point:
            if point and point.val == current.val:
                point = point.next
            elif point and point.val != current.val:
                current.next = point
                current = current.next
                point = point.next
        current.next = None
        return head
        