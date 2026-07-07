class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        start_row , end_row, start_col, end_col = [0,rows-1,0,cols-1]
        answer = []

        def spiral_traverse ( start_row, end_row, start_col, end_col, answer,matrix):
            if start_row > end_row or start_col > end_col:
                return
            if start_row ==end_row and start_col == end_col:
                answer.append(matrix[start_row][end_col])
                return
            if start_row == end_row:
                for i in range(start_col,end_col +1):
                    answer.append(matrix[start_row][i])
                return
            if start_col == end_col:
                for i in range(start_row,end_row +1):
                    answer.append(matrix[i][start_col])
                return
            
            #top row: 
            for i in range(start_col,end_col):
                answer.append(matrix[start_row][i])
            #right col
            for i in range(start_row,end_row):
                answer.append(matrix[i][end_col])
            #bottom row
            for i in range(end_col,start_col,-1):
                answer.append(matrix[end_row][i])
            #left col
            for i in range(end_row,start_row,-1):
                answer.append(matrix[i][start_col])

            print(f"spiral traversal for start row = {start_row} gives list so far = {answer}")

            return spiral_traverse(start_row+1, end_row-1, start_col+1, end_col-1, answer,matrix)
        
        spiral_traverse(start_row, end_row, start_col, end_col, answer,matrix)

        return answer


        