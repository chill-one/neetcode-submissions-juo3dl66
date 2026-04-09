# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
    d <- 0 -> 1 -> 2 -> 3
         p         c
        """
        curr, prev = head, None

        while curr:
            temp, curr = curr, curr.next
            temp.next = prev
            prev = temp

        return prev