class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)

        for i in range(n):
            y = target - nums[i]
            if y in dic:
                return [dic[y], i]
            else:
                dic[nums[i]] = i


        return []