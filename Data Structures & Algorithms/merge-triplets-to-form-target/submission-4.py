class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = target

        safe = set()
        found = [0,0,0]
        
        for arr in triplets:
            val1, val2, val3 = arr
            if val1 <= x and val2 <= y and val3 <= z :
                for i in range(3):
                    if arr[i] == target[i]:
                        safe.add(i)


        return len(safe) == 3


        




            

