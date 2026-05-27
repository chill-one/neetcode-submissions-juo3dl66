# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        DummyNode = ListNode()

        first, second = l1, l2
        curr = DummyNode
        carry = 0
        while first or second:
            firstValue = first.val if first else 0
            secondValue = second.val if second else 0
            total = firstValue + secondValue + carry
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)

            curr = curr.next
            first = first.next if first else None
            second = second.next if second else None

        if carry:
            curr.next = ListNode(carry)

        return DummyNode.next