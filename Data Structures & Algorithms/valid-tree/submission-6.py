class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        [0, 0, 1, 2, 1]

        0 - 1
        1 - 2
        2 - 3
        1 - 3
        1-  4
        """
        
        rank = [0] * n
        union = list(range(n))

        def find(node):
            root = union[node]
            # are we at the root 
            if node != root:
                #find the root for this node
                union[node] = find(root)
                return union[node]

            return root

        def unionSets(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return False

            #if x has less rank than we join x to y
            if rank[xRoot] < rank[yRoot]:
                union[xRoot] = yRoot
            elif rank[yRoot] < rank[xRoot]:
                union[yRoot] = xRoot
            else:
                union[yRoot] = xRoot
                rank[xRoot] += 1
            return True

        #Checks for no cycle
        for x , y in edges:
            if not unionSets(x, y):
                return False

        return len(edges) == n - 1
            

        

        


        


        