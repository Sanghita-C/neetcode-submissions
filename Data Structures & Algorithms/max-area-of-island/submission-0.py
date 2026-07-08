class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        [0,2,2,0,1],
        [1,0,2,0,1],
        [0,2,2,0,1],
        [0,2,0,0,1]
        """
        max_area = 0

        row = len(grid)
        col = len(grid[0])

        def dfs(grid, row_in, col_in):
            total_row = len(grid)
            total_col = len(grid[0])
            #print(f"row = {row_in} and col = {col_in}, total row = {total_row}, total col = {total_col}")

            if row_in <0 or row_in >= total_row:
                #print("row index out of bounds")
                return 0
            
            if col_in < 0 or col_in >= total_col:
                #print("col index out of bounds")
                return 0

            if grid[row_in][col_in] == 0 or grid[row_in][col_in] == 2:
                return 0
            
            grid[row_in][col_in] = 2

            #check top
            top = dfs(grid, row_in -1, col_in) #0

            #check right
            right = dfs(grid, row_in , col_in+1) 

            #check left
            left = dfs(grid, row_in , col_in-1) 

            #check bottom
            bottom = dfs(grid, row_in +1 , col_in) 

            return 1 + top+ left+ right+ bottom


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = dfs(grid, i , j)
                    max_area = max(max_area, area)

        return max_area
        