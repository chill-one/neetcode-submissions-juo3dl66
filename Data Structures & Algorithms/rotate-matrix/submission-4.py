class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        [1,2,3,4.  ]  
        [5,6,7,8.  ]
        [9,10,11,12]
        """
        N = len(matrix)
        top, bottom = 0, N-1
        left, right = 0, N-1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            left+=1
            right-=1

        









            
