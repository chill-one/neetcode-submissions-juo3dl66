class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        color_to_update = image[sr][sc]
        def dfs(r, c):
            if 0 > r or r >= len(image) or 0 > c or c >= len(image[0]):
                return 

            if image[r][c] != color_to_update:
                return

            image[r][c] = color

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dx, c + dy)


            return

        dfs(sr, sc)
        return image