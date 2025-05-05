#problem 6
def duplicates(list0):
    i=-1
    j=0
    for i in range(len(list0)):
        for j in range(i):
            if list0[i]==list0[j]:
                return True
    return False
def duplicates2(list0):
    for i in range(len(list0)):
        if list0[i]==list0[i+1]:
            return True
    return False
if __name__=='__main__':
    L=[1,1,2]
    print(duplicates2(L))
