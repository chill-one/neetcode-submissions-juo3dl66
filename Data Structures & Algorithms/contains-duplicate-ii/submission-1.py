class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0
        for right in range(len(nums)):
            if len(seen) > k:
                seen.remove(nums[l])
                l+=1
            if nums[right] in seen:
                return True

            seen.add(nums[right])

        return False
