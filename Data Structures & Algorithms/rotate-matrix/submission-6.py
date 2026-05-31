class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
         l     r
        t[1,2,3],
         [4,5,6],
        b[7,8,9]
        """


        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            left = top
            right = bottom
            for i in range(right - left):
                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp

            top +=1
            bottom -= 1
