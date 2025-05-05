import copy
#problem 1.a

def lower_case(b):
    b=b.lower()
    return b
print(lower_case("sTRING"))

#problem 1.b
L = [1, 2, 3]
print("before", id(L))
#print("before:", id(L))
def f(L):
    L[0]=1
    return L
def g1(L):
    return L
def g(L):
    L1 = L[:]
    L1=[1]
    return L1
L=f(L) #changes contents of L
print("after", id(L))
L=g(L) #changes id of L
print("after:", id(L))
L=g1(L) #doesn't change' L
print("after:", id(L))

#problem 1.c
def d_copy(d):
    d1= d.copy()
    return d1
def d_change(d):
    d1= copy.deepcopy(L)
    return d
def d_changecont(d):
    d[1] = 5
    return d
d={1:2, 2:3, 3:4}
#print("dictionary before:", id(d))
#d=d_copy(d) #changes id of d
#print("after:", id(d))
#d=d_change(d) #does not change id of d
#print("after", id(d))
#d = d_changecont(d)
#print("after", id(d))

#problem 1.d
def d_mutable(d):
    d1=d.copy()
    d1[1][2]=4
    print(d1)
    print(d)
    print("d1 id", id(d1))
d={1:[1,2,3], 2:2}
d=d_mutable(d)
print("after:", id(d))

#problem 1.e
def d_deepcopy(d):
    d1=copy.deepcopy(d)
    d1[1][2]=4
    print(d1)
    print(d)

d={1:[1,2,3], 2:2}
d=d_deepcopy(d)
print(id(d))


