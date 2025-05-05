#debugging inf loop -- do ctrl+i, go to shell -> post-mortem-> click on stack-> find where inf loop is -> go back to ur file and edit
'''def infinite_on_calc(course):
    if course == "calculus":
        while True:
           print("epsilon") #change to return "epsilon"
    else:
        return "delta"'''

#part 1
import numpy as np


def print_matrix(M_lol):
    M_lol = np.array(M_lol)
    return M_lol

M = [[1,-2,3],[3,10,1],[1,5,3]]


#part 2
'''def get_lead_ind(row): -> mine
    i=0
    for nonzero in range(len(row)):
        if row[nonzero]!=0:
            break
        else:
            i+=1
    return i'''
def get_lead_ind(row): #guerzhoy
    for i in range(len(row)):
        if row[i]!=0:
            return i
    return len(row)

#part 3


'''def get_row_to_swap(M, start_i): #change so that one condition is taht if row number is not equal to whatever get_lead_ind is, then it wont swap and then generalize it -> mine
    left_most_i = get_lead_ind(M[start_i])
    min_rows = start_i
    for rows in range(start_i+1,len(M)):
        if get_lead_ind(M[rows])<left_most_i:
            min_rows = rows
            left_most_i = get_lead_ind(M[rows])
    return min_rows'''

def get_row_to_swap(M, start_i): #guerzhoy (basically mine)
    cur_min = get_lead_ind(M[start_i]) #what is index of current row
    cur_min_i = start_i #starting with the row we began with
    for row_i in range(start_i+1, len(M)): #checking down
        cur = get_lead_ind(M[row_i]) #getting current lead ind ofeach iteration
        if cur<cur_min: #if it's smaller (i.e. needs to be swapped)
            cur_min = cur
            cur_min_i=row_i
    return cur_min_i


#part 4
def add_rows_coefs(r1,c1,r2,c2): #mine worked so i didn't change'
    for vals in range(len(r2)):
        r1[vals]*=c1
        r1[vals]+= r2[vals]*c2
    return r1



#part 5
'''def eliminate(M, row_to_sub, best_lead_ind): -> mine
    for rows in range(row_to_sub+1,len(M)):
        if get_lead_ind(M[rows]) == best_lead_ind:
            add_rows_coefs(M[rows],1,M[row_to_sub],-(M[rows][best_lead_ind])/(M[row_to_sub][best_lead_ind]))
    print(M)'''

def eliminate(M, row_to_sub, best_lead_ind): #guerzhoy's (basically the same as mine, except it actually changes the row in the function)
    for row_i in range(row_to_sub+1, len(M)):
        coef = M[row_i][best_lead_ind]/M[row_to_sub][best_lead_ind]
        new_row = add_rows_coefs(M[row_i], 1, M[row_to_sub], -coef)
        M[row_i]=new_row



#part 6
'''
def forward_step(M): -> mine
    for i in range (len(M)):
        row = get_row_to_swap(M, i)
        M[i],M[row]= M[row], M[i]
        ind = get_lead_ind(M[i])
        eliminate (M, i, ind)
        print(print_matrix(M))
    return M
    '''
def forward_step(M): #guerzhoy's (basically mine)
    for row_i in range(len(M)-1):
        row_to_swap = get_row_to_swap(M, row_i)
        M[row_i], M[row_to_swap] = M[row_to_swap], M[row_i]
        lead_ind = get_lead_ind(M[row_i])
        eliminate(M, row_i, lead_ind)
        print(print_matrix(M))
    return M
#part 7
'''def backward_step(M):
    forward_step(M)
    rows = 0
    while rows<len(M):
        lead_ind = get_lead_ind(M[rows])
        for row in range(-1, len(M)-1):
            if M[row+1][lead_ind] !=0:
                eliminate(M, rows, lead_ind)

                print(print_matrix(M))
        rows+=1
    return M'''

def eliminate1(M, row_to_sub, best_lead_ind, forward = True): #jessica's'
    lead = M[row_to_sub][best_lead_ind] # element used to eliminate
    if (forward and row_to_sub == len(M)-1): # it is last row
        return M
    elif (not forward and row_to_sub == 0): # it is first row (backward)
        return M
    # base case: forward
    start = row_to_sub + 1
    end = len(M)
    step = 1
    # backward
    if not forward:
        start = row_to_sub - 1
        end = -1
        step = -1
    for i in range(start, end, step):
        el = M[i][best_lead_ind] # element to be eliminated
        M[i] = add_rows_coefs(M[i], 1, M[row_to_sub], -el/lead)
    return M

def backward_step(M, Mb):
    # go from the bottom and eliminate all elements above lead
    for i in range(len(M)-1, -1, -1): # go row by row from bottom
        # make other elements in leading columns 0
        lead = get_lead_ind(M[i]) # lead index of current row
        if (lead != len(M[i])): # if not a zero row
            eliminate1(Mb, i, lead, forward = False)
            c1 = 1/M[i][lead]
            Mb[i] = add_rows_coefs(Mb[i], c1, Mb[i], 0)
    print(print_matrix(M))
    return M

M = [[0,2,1,1],
    [4,0,5,2],
    [8,1,7,0],
    [5,6,7,8]]

print(backward_step(M, forward_step(M)))

