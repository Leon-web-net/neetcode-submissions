# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        list_sz = 0
        
        while temp:
            temp = temp.next
            list_sz+=1
        
        m = list_sz - n
        
        i = 0
        prev = None
        curr = head

        while i<m:
            prev = curr
            curr = curr.next
            i+=1

        if prev is None:
            return head.next
        if curr.next is None:
            prev.next = None
            return head
        
        if prev and curr.next:
            prev.next = curr.next
            return head


