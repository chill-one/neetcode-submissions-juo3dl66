class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)


        val , res = 0, 0
        for key, value in freq.items():
            if value > val:
                val = value
                res = key


        return res