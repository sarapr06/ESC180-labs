'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random

def play_ttt_two_users(): #guerzhoy's code'
    board = make_empty_board()
    mark="X"
    prev_mark="0"
    while True:
        sq=int(input("Enter sq num: "))
        put_in_board(board,mark,sq)
        print_board_and_legend(board)
        print("\n\n")
        mark, prev_mark=prev_mark,mark

def board_coord(square_num):
    return [(square_num-1)//3,(square_num-1)%3] #column is index number divided by 3 (integer) and row is the mod of 3 (0,1,2)
    #e.g. 7//3=2 means 7 would be row 3. 7%3=1, so it's column 2


def put_in_board(board, mark, square_num):
    row, col = board_coord(square_num) #row is first index of coord, and col is second index
    board[row][col]=mark

def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark):
            return True
        if is_col_all_marks(board, i, mark):
            return True
    if is_diagonals_all_marked(board, mark):
            return True
    return False

def is_row_all_marks(board, row_i, mark):
    for j in range(len(board)):
        if board[row_i][j] != mark:
            return False
    return True

def is_col_all_marks(board, col_i, mark):
    for i in range(len(board[0])):
        if board[i][col_i] != mark:
            return False
    return True

def is_diagonals_all_marked(board, mark):
    count = 0
    if board[0][0]== mark and board[1][1]== mark and board[2][2] == mark:
        return True
    elif board[0][2]== mark and board[1][1]== mark and board[2][0] == mark:
        return True
    return False
def get_free_squares(board):
    free= []
    for row in range(3):
        for col in range(3):
            if board[row][col]==" ":
                free.append([row,col])
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
    random_num = int(random.random()* len(free_move))
    row = free_move[random_num][0]
    col = free_move[random_num][1]
    board[row][col] = mark
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if free_move[random_num][0]==i and free_move[random_num][1]==j:
    #             board[i][j] = mark

def play_against_random(): #guerzhoy's'
    board = make_empty_board()
    user_mark="x"
    computer_mark="0"
    mark = ""
    print_board_and_legend(board)
    while not is_win(board, "X") or not is_win(board, "0"):
        sq=int(input("Enter sq num: "))
        put_in_board(board,user_mark,sq)
        if is_win(board, "X"):
            print_board_and_legend(board)
            print("USER WON!")
            return
        is_it_a_win(board, "0")
        make_random_move(board, "0")
        if is_win(board, "0"):
            print_board_and_legend(board)
            print("COMPUTER WON!")
            return

        print_board_and_legend(board)
    i


def is_it_a_win(board, mark): #sees if there's a win'
    for row in range(3):
        for col in range(3):
            if board[row][col]==" ":
                board[row][col]=mark
                if is_win(board, mark):
                    return
                else:
                    board[row][col]==" "


def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

if __name__ == '__main__':
    board = make_empty_board()
    turnX = 2
    print_board_and_legend(board)
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    play_against_random()