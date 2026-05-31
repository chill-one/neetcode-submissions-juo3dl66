class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        res = []

        for key, value in freq.items():
            if value > len(nums) // 3:
                res.append(key)


        return res
