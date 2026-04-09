class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()
        for i in range(N):
            left, right = i + 1, N - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    
                    left += 1
                    while left < right  and nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                   
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1

                else:
                    left += 1

        return res
