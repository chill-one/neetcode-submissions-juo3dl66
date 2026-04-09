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
        """
        {7x:3x, }
        3, 7,  
        """


        new_random_node = {}
        curr = head
        new_node_head = Node(0, None, None)
        new_curr = new_node_head
        while curr:
            new_node = Node(curr.val, None, None)
            new_random_node[curr] = new_node
            new_curr.next = new_node
            new_curr = new_curr.next 
            curr = curr.next
        
        curr = head
        new_curr = new_node_head.next
        while curr:
            new_curr.random = new_random_node.get(curr.random, None)
            curr = curr.next
            new_curr = new_curr.next

        return new_node_head.next