# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if not l1:
                return l2
            if not l2:
                return l1
            
            dummy = ListNode()
            merged_list = dummy
            
            while l1 and l2:

                if l1.val>l2.val:
                    merged_list.next = l2
                    l2 = l2.next
                else:
                    merged_list.next = l1
                    l1 = l1.next
                
                merged_list = merged_list.next
            
            if l1:
                merged_list.next = l1
            else:
                merged_list.next = l2
            
            return dummy.next

