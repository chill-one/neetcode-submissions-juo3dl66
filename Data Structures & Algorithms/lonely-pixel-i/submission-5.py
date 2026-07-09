class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        Its not in the dic -> no black found 
        True -> black was just found
        {0:True, }
        {0:True}

        row not in r_dic and col not in c_dic:
            count += 1
        else:
            count -= 1

            [["W","B","W","W"],
            ["W","B","B","W"],
            ["W","W","W","W"]]
        """
        row_seen = defaultdict(int)
        col_seen = defaultdict(int)

        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] != 'B':
                    continue

                row_seen[i] += 1
                col_seen[j] += 1


        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] != 'B':
                    continue
                
                if row_seen[i] + col_seen[j] == 2:
                    count += 1


        return count
        