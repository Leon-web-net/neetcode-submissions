# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        fast = slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        first = head

        # reverse back half of list
        prev = None
        while second:
           
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # merge both lists
        while second:
            f_next,s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next
        