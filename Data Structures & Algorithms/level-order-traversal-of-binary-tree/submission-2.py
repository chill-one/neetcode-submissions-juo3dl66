# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue
        if root == None:
            return []
        q = Queue()
        res = []

        q.put(root)

        while not q.empty():
            window = []
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                window.append(curr.val)
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
            res.append(window)
        return res