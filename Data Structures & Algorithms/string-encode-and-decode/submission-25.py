class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f"{len(string)}#{string}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j+=1
            print(s[i])
            length = int(s[i:j])
            string = s[j+1: j+length+1]
            res.append(string)

            i = j + length +1
        return res
