class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = Counter(nums)

        count = 0
        for n in nums:
            val = n + 1
            curr_count = 1
            while val in freq:
                curr_count += 1
                val += 1

            count = max(curr_count, count)

        return count


