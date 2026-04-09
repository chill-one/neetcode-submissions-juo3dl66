# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = None, head

        while(fast != None and fast.next != None):
            if slow == fast:
                return True

            fast = fast.next.next
            slow = head if slow == None else slow.next

        return False
        