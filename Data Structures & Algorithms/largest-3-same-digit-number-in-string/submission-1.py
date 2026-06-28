class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = float('-inf')

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_num = max(max_num, int(num[i]))


        return "" if max_num == float('-inf') else str(max_num) * 3