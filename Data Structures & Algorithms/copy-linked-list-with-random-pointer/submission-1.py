"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None: None}
        """
            3 : new 3 
            7 : new 7 
            4 : new 4
            5 : new 5


            dummyNode -> 3(null) -> 7(5)

        """


        curr = head
        while curr:
            map[curr] = Node(curr.val, curr.next, None)
            curr = curr.next



        dummyNode = Node(-1)

        newCurr = dummyNode        
        curr = head
        while curr:
            newCurr.next = map[curr]
            map[curr].random = map[curr.random]

            newCurr = newCurr.next
            curr = curr.next


        return dummyNode.next


        

            