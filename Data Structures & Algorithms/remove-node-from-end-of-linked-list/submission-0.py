# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        move = 1
        while first != None and move <= n :
            first = first.next
            move += 1

        dummy = ListNode(0,head)
        second = dummy
        while first != None:
            first = first.next
            second = second.next 
        
        second.next = second.next.next

        return dummy.next