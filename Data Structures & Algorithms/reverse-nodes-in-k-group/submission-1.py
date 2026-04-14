# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        k = 3
        d -> 1 -> 2 -> 3 -> 4 -> 5
        p              k

        6 <- 5 <- 4 <- 1 <- 2 <- 3 
                            kth
        """
        DummyNode = ListNode(-1, head)
        prev, curr = DummyNode, head

        while True:
            val = self.getKthNode(prev, k)
            if not val:
                break
            next_comp = val.next
            p, c = next_comp , curr

            for i in range(k):
                temp = c.next
                c.next = p
                p = c
                c = temp

            temp = prev.next
            prev.next = val
            prev = temp

            curr = next_comp

        return DummyNode.next
            
            
    def getKthNode(self, head, k):
        curr = head
        for i in range(k):
            if curr:
                curr = curr.next

        return curr


        