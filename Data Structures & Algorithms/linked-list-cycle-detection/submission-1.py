# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head:

            if head.next is False:
                return True
            if head.next is None:
                return False

            temp = head.next
            head.next = False
            head = temp
        
        return False
        
