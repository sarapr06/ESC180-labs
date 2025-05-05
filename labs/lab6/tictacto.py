'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random
def playing():
    global turnX
    print("\n\n")
    mark = ""
    turn_num = 0

    print_board_and_legend(board)
    if turn_num==10:
        return "draw!"
    while turn_num<10:
        can_i_put = True
        if turn_num%2==0:
            mark = ask_forX_or0()
            input_coord = int(input("please enter a coordinate between 1 and 9: "))

            put_in_board(board, mark, input_coord)
            print("\n\n")
            print_board_and_legend(board)
            turnX+=1
            turn_num +=1
            if is_win(board, mark):
                print(mark + " won!")
                return mark

        else:
            if turnX%2 == 0:
                mark = "X"
            else:
                mark = "0"
            make_random_move(board, mark)
            if is_it_a_win(mark):
                print("\n\n")
                print_board_and_legend(board)
                print(mark + " won!")
                return mark
            print("\n\n")
            print_board_and_legend(board)
            turnX+=1
            turn_num+=1
            if is_win(board, mark):
                print(mark + " won!")
                return mark


def ask_forX_or0():
    global turnX
    input_str=""
    if turnX%2==0:
        while input_str!="X":
            input_str = input("Please enter your player mark: ")
        return "X"
    else:
        while input_str!="0":
            input_str = input("Please enter your player mark: ")
        return "0"



def board_coord(square_num):
    coord = []
    if square_num == 1 or square_num == 2 or square_num == 3:
        coord.append(0)
        coord.append((square_num-1))
    elif square_num == 4 or square_num == 5 or square_num == 6:
        coord.append(1)
        coord.append((square_num-4))
    elif square_num == 7 or square_num == 8 or square_num == 9:
        coord.append(2)
        coord.append((square_num-7))
    return coord
def put_in_board(board, mark, square_num):
    coord = board_coord(square_num)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if coord[0]==i and coord[1]==j:
                board[i][j] = mark

def is_win(board, mark):
    for i in range(2):
        if is_row_all_marks(board, i, mark):
            return True
        if is_col_all_marks(board, i, mark):
            return True
        if is_diagonals_all_marked(board, mark):
            return True
    return False
def is_row_all_marks(board, row_i, mark):
    count = 0
    for j in range(len(board)):
        if board[row_i][j] == mark:
            count+=1
    if count == 3:
        return True
    else:
        return False
def is_col_all_marks(board, col_i, mark):
    count = 0
    for j in range(len(board[0])):
        if board[j][col_i] == mark:
            count+=1
    if count == 3:
        return True
    else:
        return False
def is_diagonals_all_marked(board, mark):
    count = 0
    if board[0][0]== mark and board[1][1]== mark and board[2][2] == mark:
        return True
    elif board[0][2]== mark and board[1][1]== mark and board[2][0] == mark:
        return True
    return False
def get_free_squares(board):
    free= []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="":
                free.append([i,j])
    return free


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
def make_random_move(board, mark):
    free_move=get_free_squares(board)
    random_num = int(3 * random.random())
    free_move[random_num]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if free_move[random_num][0]==i and free_move[random_num][1]==j:
                board[i][j] = mark
def where_am_i(L):
    square_num = 0
    if L[0]==0 and L[1]==0:
        square_num = 1
    elif L[0]==0 and L[1]==1:
        square_num = 2
    elif L[0]==0 and L[1]==2:
        square_num = 3
    elif L[0]==1 and L[1]==0:
        square_num = 4
    elif L[0]==1 and L[1]==1:
        square_num = 5
    elif L[0]==1 and L[1]==2:
        square_num = 6
    elif L[0]==2 and L[1]==0:
        square_num = 7
    elif L[0]==2 and L[1]==1:
        square_num = 8
    elif L[0]==2 and L[1]==2:
        square_num = 9
    return square_num
def is_it_a_win(mark):
    free_squares = get_free_squares(board)
    for i in range(len(free_squares)):
        square_num = where_am_i(free_squares[i])
        put_in_board(board, mark, square_num)
        if is_win(board, mark):
            return True
        elif not is_win(board, mark):
            put_out_board(square_num)
            return False


def put_out_board(square_num):
    coord = board_coord(square_num)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if coord[0]==i and coord[1]==j:
                board[i][j] = ""
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

if __name__ == '__main__':
    board = make_empty_board()
    turnX = 2
    print_board_and_legend(board)
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    playing()