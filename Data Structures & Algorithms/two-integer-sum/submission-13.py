class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            y = target - nums[i]

            if y in dic:
                return [dic[y], i]

            dic[nums[i]] = i


        return None