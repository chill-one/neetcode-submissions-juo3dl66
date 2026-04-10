class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity

        self.head = Node()
        self.tail = Node()

        #Set the dummyNode for head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    Inserts the given node at the front of the doubly linked list
    """
    def insert(self, node) -> None:
        left, right = self.head, self.head.next
        left.next = right.prev = node
        node.next, node.prev = right, left

    """
    Remove the given node
    """
    def remove(self, node) -> Node:
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

        return node


    def get(self, key: int) -> int:
        """
        to do 
        x after getting the key, put it to the top of the list
        x Returns the value corresponding to the key
        """
        print(self.dic)
        if key in self.dic:
            value = self.dic[key]
            self.remove(value)
            self.insert(value)
            return value.val

        return -1


    def put(self, key: int, value: int) -> None:
        """
        remove if element if it  exists
        Add if it does not exits
        if new pair results in the length being larger than cap evict the first value 
        in the doubly linked list
        """
        if key in self.dic:
            self.remove(self.dic[key])

        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])

        if len(self.dic) > self.cap:
            lru = self.remove(self.tail.prev)
            del self.dic[lru.key]

        
