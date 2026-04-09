class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-4, -1, -1, 0, 1, 2]
        """
        number = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            left, right = i + 1, n - 1
            if i > 0 and number[i - 1] == number[i]:
                continue
            
            while left < right:
                if number[i] + number[left] + number[right] == 0:
                    res.append([number[i], number[left], number[right]])
                    left += 1
                    right -= 1
                    while number[left] == number[left - 1] and left < right:
                        left += 1
                    while number[right] == number[right + 1] and left < right:
                        right -= 1
                elif number[i] + number[left] + number[right] < 0:
                    left += 1
                else:
                    right -= 1

        return res