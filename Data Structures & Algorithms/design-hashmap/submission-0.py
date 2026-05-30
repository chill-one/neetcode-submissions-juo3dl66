class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.arr = [None for _ in range(2)]
        self.length = 0

    def addToArray(self, arr, idx, key, value):
        if not arr[idx]:
            arr[idx] = Node()

        curr = arr[idx]
        while curr.next:
            if curr.key == key:
                break
            curr = curr.next
        if curr.key == key:
            curr.value = value
            return
            
        curr.next = Node(key, value)
        self.length += 1

    def double(self):
        newCap = len(self.arr) * 2
        newArray = [None for _ in range(newCap)]

        for value in self.arr:
            curr = value.next if value else None
            while curr:
                idx = curr.key % newCap
                self.addToArray(newArray, idx, curr.key, curr.value)
                curr = curr.next

        self.arr = newArray

    def put(self, key: int, value: int) -> None:
        if self.length > len(self.arr):
            self.double()

        idx = key % len(self.arr)
        self.addToArray(self.arr, idx, key, value)
        

    def get(self, key: int) -> int:
        idx = key % len(self.arr)

        curr = self.arr[idx]
        if not curr:
            return -1

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

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


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)