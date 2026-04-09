class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx in range(len(nums)):
            y = target - nums[idx]

            if y in dic:
                return [dic[y], idx]

            dic[nums[idx]] = idx


        return None