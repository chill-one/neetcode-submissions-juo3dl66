class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [None for _ in range(2)]
        self.length = 0

    def double(self):
        newCap = len(self.arr) * 2
        newArray = [None for _ in range(newCap)]

        for value in self.arr:
            curr = value.next if value else None
            while curr:
                idx = curr.key % newCap
                self.addToArray(newArray, idx, curr.key)
                curr = curr.next

        self.arr = newArray

    def addToArray(self, arr, idx, key):
        if not arr[idx]:
            arr[idx] = Node()

        curr = arr[idx]
        while curr.next:
            curr = curr.next
        curr.next = Node(key)
        self.length += 1


    def add(self, key: int) -> None:
        if self.contains(key):
            return
        if self.length > len(self.arr):
            self.double()

        idx = key % len(self.arr)
        self.addToArray(self.arr, idx, key)

    def remove(self, key: int) -> None:
        idx = key % len(self.arr)

        curr = self.arr[idx]
        if not curr:
            return
        prev = None
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        self.length -= 1
        

    def contains(self, key: int) -> bool:
        idx = key % len(self.arr)

        curr = self.arr[idx]
        if not curr:
            return False

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)