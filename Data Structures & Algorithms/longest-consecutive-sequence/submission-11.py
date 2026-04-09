class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}

        longest_seq = 0
        for num in nums:
            if num in dic:
                continue
            curr_seq = 1

            incr = num + 1
            while(incr in dic):
                curr_seq+=1
                incr+=1

            dcr = num - 1
            while(dcr in dic):
                curr_seq += 1
                dcr -= 1
            longest_seq = max(longest_seq, curr_seq)

            dic[num] = True

        return longest_seq
