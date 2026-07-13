class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        [1,2,4,5]
        l.     r
        """
        people.sort()
        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            val = people[l] + people[r]
            if val <= limit:
                l = l + 1
                r = r - 1
                res+=1
            else:
                res += 1
                r = r - 1

        return res
