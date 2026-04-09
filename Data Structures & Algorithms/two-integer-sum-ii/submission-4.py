class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(numbers)):
            look_up = target - numbers[i]
            if look_up in dic:
                return [dic[look_up] + 1, i + 1]
            dic[numbers[i]] = i

        return None