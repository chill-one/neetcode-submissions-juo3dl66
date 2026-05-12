class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        aab
        a    aa      aab
    a ab   aa b      
b 
        """
        res = []


        def dfs(end, arr):
            if end >= len(s):
                res.append(arr)
                return

            for i in range(end, len(s)):
                string = s[end: i+1]
                if string == string[::-1]:
                    arr.append(string)
                    dfs(i + 1, arr[:])
                    arr.pop()

    

        dfs(0, [])
        return res

                
            
            


            