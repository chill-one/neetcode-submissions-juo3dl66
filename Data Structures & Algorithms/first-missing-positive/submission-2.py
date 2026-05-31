class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        nums.sort()

        for idx in range(len(nums)-1):
            if nums[idx] < 0:
                continue

            if nums[idx + 1] - nums[idx] > 1:
                return nums[idx] + 1


        return nums[-1] + 1


            