class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0 for i in range(26)]

        for char in s:
            arr[ord(char) - ord('a')]+=1

        for char in t:
            arr[ord(char) - ord('a')]-=1


        for num in arr:
            if num != 0:
                return False


        return True

        