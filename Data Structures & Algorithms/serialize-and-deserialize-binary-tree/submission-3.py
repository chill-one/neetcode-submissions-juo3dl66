# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        def dfs(curr):
            if not curr:
                s.append("N")
                return

            s.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ",".join(s)

         

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        1,2,N,N,3,4,N,N,5,N,N

        2,N,N,3,4,N,N,5,N,N
        N,N,3,4,N,N,5,N,N.          N,3,4,N,N,5,N,N
        """
        """
                       1
                2.       
            N     N
                
        """
        q = deque(data.split(","))
        def dfs():
            val = q.popleft()
            currNode = None
            if val.isdigit():
                currNode = TreeNode(int(val))
                currNode.left = dfs()
                currNode.right = dfs()

            return currNode

        return dfs()



        
