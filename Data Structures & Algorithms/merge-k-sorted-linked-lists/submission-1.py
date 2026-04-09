# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSortedList(list1, list2):
            first, second = list1, list2
            new_list = ListNode()
            curr = new_list
            while first and second:
                if first.val < second.val:
                    curr.next = first
                    first = first.next
                else:
                    curr.next = second
                    second = second.next

                curr = curr.next

            if first:
                curr.next = first
            if second:
                curr.next = second

            return new_list.next
        res = lists[0] if lists else None
        for idx in range(1, len(lists)):
            res = mergeSortedList(res, lists[idx])

        return res
