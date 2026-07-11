class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx, num in enumerate(nums):
            y = target - num

            if y in dic:
                return [dic[y], idx]

            dic[num] = idx


        return [-1, -1]
            