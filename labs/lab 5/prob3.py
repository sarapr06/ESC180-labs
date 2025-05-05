#prob 3:

def lists_are_the_same(list1, list2):
    greater = 0
    e=0
    for e in range(len(list1)):
        if list1[e] != list2[e]:
            return False
    return True

if __name__=='__main__':
    L=[0,1,2,3]
    L2=[0,1,2,3]
    print(lists_are_the_same(L,L2))