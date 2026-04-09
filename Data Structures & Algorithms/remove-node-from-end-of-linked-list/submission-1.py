# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        DummyNode = ListNode(-1)

        DummyNode.next = head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        length  = length - n
        print(length)

        prev, curr = DummyNode, head,

        while curr:
            if length == 0:
                prev.next = curr.next

            prev, curr = curr, curr.next
            length -= 1

        return DummyNode.next
            

        