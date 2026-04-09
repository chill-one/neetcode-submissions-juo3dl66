class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
