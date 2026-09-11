class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """

        - rows
        - cols
        - boxes

        set = []
        row 
        i =0 row. to n rows:

            - set=  []
            - count = 0
            j = 0 to m col:
            - if not . : 
                - put the jth element 
                - count ++
                - check if the len of set = count

        
        box_x, box_y

        box_x :
            box_y: 
                i -> 3*box_x to 2+3*box_x:
                    j ->3 * box_y to 2+ 3*box_y:


        """

        #row check 

        row = len(board)
        col = len(board[0])

        for i in range(row):
            num_set = set()
            num_count = 0
            for j in range(col):
                if board[i][j] != ".":
                    num_count += 1
                    num_set.add(board[i][j])
                    if len(num_set)!= num_count:
                        return False

        #col check 

        for j in range(col):
            num_set = set()
            num_count = 0
            for i in range(row):
                if board[i][j] != ".":
                    num_count += 1
                    num_set.add(board[i][j])
                    if len(num_set)!= num_count:
                        return False

        #box checks
        box_x, box_y = [0,0]

        for box_x in range(3):
            for box_y in range(3):
                num_set = set()
                num_count = 0
                for i in range(3*box_x, 3*(1+box_x)):
                    for j in range(3*box_y, 3*(1+box_y)):
                        if board[i][j] != ".":
                            num_count += 1
                            num_set.add(board[i][j])
                            if len(num_set)!= num_count:
                                return False

        
        return True



        