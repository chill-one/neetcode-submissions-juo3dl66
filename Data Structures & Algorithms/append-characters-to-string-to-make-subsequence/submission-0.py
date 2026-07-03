class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        a b c d e
        z
        """

        q = deque(list(s))

        need = 0
        pos = 0

        while q and pos < len(t):
            value = q.popleft()

            if value == t[pos]:
                pos += 1


        return len(t) - pos 
            

            
            
