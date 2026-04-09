# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeList(self, l1, l2):
        dummyNode = ListNode()
        tail = dummyNode
        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next

        while curr1:
            tail.next = curr1
            tail, curr1 = tail.next, curr1.next

        while curr2:
            tail.next = curr2
            tail, curr2 = tail.next, curr2.next

        return dummyNode.next

        
        
                