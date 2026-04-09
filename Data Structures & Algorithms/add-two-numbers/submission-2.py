# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = l1, l2
        head = ListNode(-1)
        curr = head

        carry = 0
        while first or second:
            first_val = first.val if first else 0
            second_val = second.val if second else 0
            curr_val = first_val + second_val + carry
            carry = curr_val // 10
            val = curr_val % 10
            curr.next = ListNode(val)

            curr = curr.next
            first = first.next if first else None
            second = second.next if second else None

        if carry:
            curr.next = ListNode(carry)

        return head.next
