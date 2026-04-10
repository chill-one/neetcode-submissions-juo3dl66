# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        def merge(list1, list2):
            dummyNode = ListNode()
            curr1, curr2, curr = list1, list2, dummyNode
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next

                curr = curr.next

            if curr1:
                curr.next = curr1
            if curr2:
                curr.next = curr2

            return dummyNode.next

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                first, second = lists[i], lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(merge(first, second))

            lists = merged_lists
        return lists[0] if lists else None




