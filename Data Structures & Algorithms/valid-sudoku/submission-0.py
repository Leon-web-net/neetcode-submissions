class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_ROWS = 9
        BOARD_COLS = 9
        board_set = set()

        for board_row in board:
            board_set.clear()
            for s in board_row:
                if s ==".":
                    continue
                
                if s in board_set:
                    print(board_set)
                    return False

                board_set.add(s)

        for col in range(BOARD_COLS):
            board_set.clear()
            for row in range(BOARD_ROWS):
                s = board[row][col]
                if s ==".":
                    continue
                
                if s in board_set:
                    return False
                board_set.add(s)
        
        for box_row in range(3):
            for box_col in range(3):
                board_set.clear()
                
                for r in range(box_row*3, box_row*3+3):
                    for c in range(box_col*3, box_col*3 +3):
                        s = board[r][c]
                        if s==".":
                            continue
                        if s in board_set:
                            return False
                        board_set.add(s)
        
        return True

        
        

    
        