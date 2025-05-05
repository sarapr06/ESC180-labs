#problem 4:
def list1_start_with_list2(list1,list2):
    if len(list1)>=len(list2):
        for e in range(len(list2)):
            if list2[e]!=list1[e]:
                return False
        return True
    else:
        return False
    #True iff list1 at least as long as list2, and the first len(list2) elements of list1 are the same as list2.

if __name__=='__main__':
    L1=[1,2, 3,7,8]
    L2=[1,2,3]
    print(list1_start_with_list2(L1,L2))
