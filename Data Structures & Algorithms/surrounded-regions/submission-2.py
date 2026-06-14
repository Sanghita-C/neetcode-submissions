class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        1) we will go through the matrix:
            - 0 means start Graph traversal to check criteria for surrounding 
                - mark visited
                - maintain a list of indexes for the region
            - traverse the list of indexes and mark them as X if the region is surrounding
        """

        row = len(board)
        col = len(board[0])
        visited = [[0]*col for i in range(row)]
        memory_surrounding = [[-1]*col for i in range(row)]

        def dfs(r_in, col_in, visited, region_node, row, col, board):
            
            #### visited[r_in][col_in] = 1
            #### region_node.append([r_in,col_in]) -- check
            
            if col_in == -1 or col_in ==  col:
                return False
            if r_in == -1 or r_in == row:
                return False
            if board[r_in][col_in] == 'X':
                return True
            region_node.append([r_in,col_in])
            if visited[r_in][col_in] == 1:
                print( "visited already row and col ", r_in, col_in)
                print("board value", board[r_in][col_in])
                print(memory_surrounding[r_in][col_in])
                if memory_surrounding[r_in][col_in] == -1:
                    return True
                return memory_surrounding[r_in][col_in]
            print( "processing row and col ", r_in, col_in)
            print("board value", board[r_in][col_in])
            visited[r_in][col_in] = 1
            # check right
            surr_b = dfs(r_in+1, col_in, visited, region_node, row, col, board)         
            # check left
            surr_t = dfs(r_in -1, col_in, visited, region_node, row, col, board)
            # check top 
            surr_l = dfs(r_in, col_in-1, visited, region_node, row, col, board)
            # check bottom
            surr_r = dfs(r_in, col_in +1, visited, region_node, row, col, board)

            memory_surrounding[r_in][col_in] =  1 if surr_r and surr_l and surr_b and surr_t else 0
            print(f"memory for {r_in} and {col_in} index is : {memory_surrounding[r_in][col_in]}" )
            return memory_surrounding[r_in][col_in]

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and visited[i][j] ==0:
                    region_node = []
                    print("dfs entering at", i, j)
                    surrounding = dfs(i,j,visited, region_node, row, col, board)
                    
                    print ("surrounding flag for the dfs node", surrounding)
                    if surrounding:
                        #print("surr is true")
                        for region in region_node:
                            board[region[0]][region[1]] = 'X'

        return


        