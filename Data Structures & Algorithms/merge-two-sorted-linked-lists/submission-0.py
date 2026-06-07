# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        start = returnList = ListNode()
        while list1 and list2:
            if list1.val< list2.val:
                
                returnList.next = list1
                list1=list1.next
            else:
                returnList.next = list2
                list2 = list2.next
            returnList = returnList.next
        
        returnList.next = list1 or list2
        return start.next