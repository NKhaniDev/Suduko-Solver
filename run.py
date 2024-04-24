#creat duduko table

def creat_sudoku_board():
    sudoku_board=[]

    for i in range(1,10):
        row=getting_row_values(i)
        sudolu_board.append(row)
    return sudoku_board    
