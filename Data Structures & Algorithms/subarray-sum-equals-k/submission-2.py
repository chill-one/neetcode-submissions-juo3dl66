class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in dic:
                count += dic[prefix - k]
            dic[prefix] += 1
            

        return count

        
        

            