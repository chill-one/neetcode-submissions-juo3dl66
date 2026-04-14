# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = deque()
        queue.append(root)

        while queue:
            p = queue.popleft()
            if not p:
                continue
            p.right, p.left = p.left, p.right

            queue.append(p.left)
            queue.append(p.right)

        return root
