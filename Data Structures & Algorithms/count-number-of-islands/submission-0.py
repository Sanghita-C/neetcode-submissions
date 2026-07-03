class Solution:
    def dfs(self, row_idx, col_idx, visited, grid ):
        visited[row_idx][col_idx] = 1
        rows = len(grid)
        cols = len(grid[0])

        #top
        if row_idx-1>=0 and grid[row_idx-1][col_idx]=="1" and visited[row_idx-1][col_idx]==0:
            #print(f"checking top of {row_idx},{col_idx}")
            self.dfs(row_idx-1,col_idx,visited,grid)
        #bottom
        if row_idx+1 < rows and grid[row_idx+1][col_idx]=="1" and visited[row_idx+1][col_idx]==0:
            #print(f"checking bottom of {row_idx},{col_idx}")
            self.dfs(row_idx+1,col_idx,visited,grid)
        #left
        if col_idx-1>=0 and grid[row_idx][col_idx-1]=="1" and visited[row_idx][col_idx-1]==0:
            #print(f"checking left of {row_idx},{col_idx}")
            self.dfs(row_idx,col_idx-1,visited,grid)
        #right
        if col_idx+1 <cols and grid[row_idx][col_idx+1]=="1" and visited[row_idx][col_idx+1]==0:
            #print(f"checking right of {row_idx},{col_idx}")
            self.dfs(row_idx,col_idx+1,visited,grid)

        return
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        [1,1] - single island
        if everything is 0 then no island

        #DFS : 
        - grid[i] == 1 and visited[i] == 0-> DFS (i)- mark visited -> count ++
        """

        row = len(grid)
        col = len(grid[0])
        island_count = 0

        visited  = [[0]*col for i in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] =="1" and visited[i][j] ==0:
                    print(f"node [{i} , {j}] being processed")
                    self.dfs(i,j,visited,grid)
                    island_count +=1
        
        return island_count
         