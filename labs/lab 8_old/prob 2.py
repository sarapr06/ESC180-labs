#prob 2
L = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

def mod1(L,a):
    L1 = []
    a = str(a)
    str1 = ""
    for i in range (len(L)):
        for j in range(len(L[0])):
            x = str(L[i][j])
            str1 += x
    for j in range (0,len(L[0])):
        str1[L[0][j]] = a
        y = str1
        L1.append(y)
    return L1

print(L)
print (mod1(L,2))