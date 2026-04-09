# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        from queue import Queue
        res = []
        q = Queue()
        q.put(root)
        res.append(str(root.val))

        while not q.empty():
            curr = q.get()
            if curr.left: 
                q.put(curr.left)
            if curr.right: 
                q.put(curr.right)

            res.append(str(curr.left.val) if curr.left else "N")
            res.append(str(curr.right.val) if curr.right else "N")

        return " ".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        from queue import Queue
        
        q = Queue()
        root = TreeNode(int(data[0]))
        q.put(root)
        data_arr = data.split(" ")
        idx = 1
        while not q.empty():
            curr = q.get()

            if idx < len(data_arr) and data_arr[idx] != "N":
                val = int(data_arr[idx])
                curr.left = TreeNode(val)
                q.put(curr.left)
            
            if idx + 1 < len(data_arr) and data_arr[idx + 1] != "N":
                val = int(data_arr[idx + 1])
                curr.right = TreeNode(val)
                q.put(curr.right)

            idx += 2

        return root

            
        


            
        

