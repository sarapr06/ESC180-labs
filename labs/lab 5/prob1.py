#prob 1
def count_evens(L):
    s=0
    for e in L:
        if e%2==0:
            s+=1
        else:
            s
    return s
    #counts number of even integers in list L

if __name__=='__main__':
    L = [0,1,2,3,4,5, 6, 8, 9]
    print(count_evens(L))
