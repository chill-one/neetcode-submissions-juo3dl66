class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        need = defaultdict(int)
        for char in t:
            need[char] += 1

        start, length = 0, len(s)+1
        left = 0
        current = defaultdict(int)
        current_count = 0

        for right, char in enumerate(s):
            print(char)
            if char in need:
                current[char] += 1
                if need[char] == current[char]:
                    current_count += 1

                while current_count == len(need):
                    curr_length = right - left + 1

                    if curr_length < length:
                        length = curr_length
                        start = left


                    left_val = s[left]
                    if left_val in need:
                        current[left_val] -= 1
                        if current[left_val] < need[left_val]:
                            current_count -= 1

                    left+= 1
            
        return s[start: start+length] if length < len(s) + 1 else ""


                



        