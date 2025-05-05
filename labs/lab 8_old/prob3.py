#prob 3
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)

def is_sq_in_board(board, y, x):
    if (y<len(board) and y>=0) and (x<len(board[0]) and x>=0):
        return True
    return False
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x
def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x): #true if seq of exactly length stones starting at
    L=[]
    for i in range(length):
        coords = []
        if y_start + d_y*i==len(board) or y_start + d_y*i<0 or x_start + d_x*i==len(board) or x_start + d_x*i<0:
            return False
        coords.append(y_start + d_y*i)
        coords.append(x_start+d_x*i)
        L.append(coords)
    if len(L)!= length:
        return False
    for e in range(length):
        if board[L[e][0]][L[e][1]] != col:
            return False
    return True

board = make_empty_board(8)
put_seq_on_board(board, 4, 7, 1, 0, 4, "w")
print_board(board)
print(is_sequence_complete(board, "w", 4, 7, 4, 1, 0))
