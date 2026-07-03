class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        # Transpose along first diagonal
        for i in range(rows):
            for j in range(cols):
                if j>=i :
                    original_value = matrix[i][j]
                    mirror_value = matrix[j][i]
                    matrix[i][j] = mirror_value
                    matrix[j][i] = original_value

        
        
        #mirror columns 

        for j in range(int(cols/2)):
            for i in range(rows):
                original_value = matrix[i][j]
                mirror_value = matrix[i][cols-1-j]
                matrix[i][j] = mirror_value
                matrix[i][cols-1-j] = original_value



        return 