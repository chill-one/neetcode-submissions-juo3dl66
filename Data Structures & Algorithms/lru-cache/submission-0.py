class Node:
    def __init__(self,key=-1, val= -1, next=None, prev=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next



class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next,prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        curr_node = self.dic[key]
        self.remove(curr_node)
        self.insert(curr_node)
        return curr_node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
            
        self.dic[key] = Node(key, value)
        curr = self.dic[key]
        self.insert(curr)

        if len(self.dic) > self.cap:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.dic[lru_node.key]
        

        
        

        
