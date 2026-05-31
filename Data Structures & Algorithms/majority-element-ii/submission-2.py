class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        [5,2,3,2,2,2,2,5,5,5]


        """
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
            if len(dic) == 3:
                new_count = defaultdict(int)
                for key, value in dic.items():
                    if value > 1:
                        new_count[key] = value - 1
                dic = new_count

        res = []
        for n in dic:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
