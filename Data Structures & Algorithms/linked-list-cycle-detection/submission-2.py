# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_ptr, slow_ptr = head, head

        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

            if fast_ptr == slow_ptr:
                return True
        return False