class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0 for _ in range(len(nums)*2)]


        for i in range(len(nums)):
            newNums[i] = nums[i]
            newNums[i+len(nums)] = nums[i]

        return newNums