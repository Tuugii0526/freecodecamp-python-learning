# sudoku
#  rules : 1.in one column , there should be 1 to 9 . in one row , there should be 1 to 9. in 3*3 square , there should be 1 to 9 . 
# we might want to solve the sudoku by backtracking . 
class Sudoku: 
    def __init__(self,board):
        self.board=board
    def __str__(self):
        board_str=''
        for row in self.board:
            row_str=[str(i) if i else '*' for i in row]
            board_str+=' '.join(row_str)
            board_str+='\n'
        return board_str
    def next_empty(self):
        for row in range(0,9):
            try:
                col=self.board[row].index(0)
                return row,col
            except ValueError:
                pass
        return None
    def valid_in_row(self,row,num):
        return num not in self.board[row]
    def valid_in_col(self,col,num):
        return all(num !=self.board[row][col] for row in range(0,9))
    def valid_in_square(self,row,col,num):
        row_start=(row//3)*3
        col_start=(col//3)*3
        for row_no in range(row_start,row_start+3):
            for col_no in range(col_start,col_start+3):
                if self.board[row_no][col_no]==num:
                    return False
        return True
    def valid(self,empty,num):
        row,col=empty
        valid_in_row=self.valid_in_row(row,num)
        valid_in_col=self.valid_in_col(col,num)
        valid_in_square=self.valid_in_square(row,col,num)
        return all([valid_in_row,valid_in_col,valid_in_square])
    def solver(self):
        if (next_empty:=self.next_empty()) is None:
            return True
        for guess in range(1,10):
            if self.valid(next_empty,guess):
                row,col=next_empty
                self.board[row][col]=guess
                if self.solver():
                    return True
                self.board[row][col]=0
                
        return False
        
def solve_sudoku(board):
    gameboard=Sudoku(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is not solvable')
    return gameboard
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0], 
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)