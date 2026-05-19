class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = target

        safe = set()
        found = [0,0,0]
        
        for arr in triplets:
            val1, val2, val3 = arr
            if val1 <= x and val2 <= y and val3 <= z :
                if val1 == x:
                    found[0] += 1
                    
                if  val2 == y:
                    found[1] += 1

                if val3 == z:
                    found[2] += 1
                safe.add((val1, val2, val3))


        for count in found:
            if count == 0:
                return False

        return True 


        




            

