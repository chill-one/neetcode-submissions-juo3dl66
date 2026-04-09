# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0 1 2 3 
        
        6 5 4 
              

        0 1 2 6 5 4 3
        """
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None
        
        prev, curr = None, second_half

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        curr, curr2 = head, prev

        while curr and curr2:
            temp1 = curr.next
            temp2 = curr2.next

            curr.next = curr2
            curr2.next = temp1
            curr = temp1
            curr2 = temp2



        

