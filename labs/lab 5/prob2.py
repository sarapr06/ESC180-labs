#PROBLEM 2
def list_to_str(lis):
    str_lis="["
    for e in range(len(lis)):
        if e+1==len(lis):
            str_lis += str(lis[e])
        else:
            str_lis += str(lis[e]) + ","

    str_lis+="]"
    return str_lis

if __name__=='__main__':

    L=[0,1,2,3,4,5]
    print(list_to_str(L))
    print('[0,1,2,3,4,5]'==list_to_str(L))