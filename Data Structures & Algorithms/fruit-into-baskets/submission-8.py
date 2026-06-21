class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0

        dic = {}
        count = 0
        for right, fruit in enumerate(fruits):
            dic[fruit] = dic.get(fruit, 0) + 1
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    dic.pop(fruits[left])
                left += 1
            
            print(left, right , dic)
            count = max(count, right - left + 1)

        return count
