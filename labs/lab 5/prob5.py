#problem 5
def match_pattern(list1,list2):
    i=0
    for i in range(len(list1)-len(list2)-1):
        if list1[i:i+len(list2)]==list2:
                return True
    return False

if __name__=='__main__':
    L1=[0,1,2,3,4]
    L2=[1,2]
    print(match_pattern(L1,L2))

