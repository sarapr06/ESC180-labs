#problem 1
def power(x, n):
    if n==0:
        return 1
    return 1*power(x, n-1)*x

print(power(2,3))


#problem 2:
def sum_digs(n):
    if len(str(n))==1:
        return n
    return int(str(n)[len(str(n))-1]) + sum_digs(int(str(n)[:len(str(n))-1]))
print(sum_digs(1238))

#guerzhoy:
def sum_digits(n):
    #base case:
        #if n is <10, just return n
    if n<10:
        return n
    #recursive step:
        #sum digits(n) is sum_digits(1...(k-1st digit of n) + last digit of n
    last_digit = n%10 #eg takes 6 from 456
    digits1_km1 = (n-last_digit)/10 #(456-6)/10=45
    return last_digit+sum_digits(digits1_km1)


#problem 3 -- REVIEWWW
# def splitter(L, num):
#     L1=[]
#     L2=[]
#     Lnew=[]
#     for e in range(len(L)):
#         if L[e] == num:
#             L[e]=""
#     for e in range(len(L)):
#         if L[e]=="":
#             L1=L[:e]
#             L2=L[e+1:]
#     Lnew.append(L1)
#     Lnew.append(L2)
#     return Lnew
# print(splitter([1,2,3,3,3,4], 3))



def splitter(L,sep):
    for i in range(len(L)):
        if L[i]==sep[1]:
            L[i]=sep[0]
    return L


def split_by_num(L, sep):
    L=splitter(L,sep)
    Lnew=[]
    lower_bound=-1
    upper_bound = 0
    for i in range(len(L)):
        if L[i] == sep[0]:
            upper_bound = i
            Lnew.append(L[lower_bound+1:upper_bound])
            lower_bound = i
    Lnew.append(L[upper_bound+1:])
    Lnew1 = []
    for i in range(len(Lnew)):
        if Lnew[i]!=[]:
            Lnew1.append(Lnew[i])
    return Lnew1
    # for i in range(len(sep)):
    #     if i==0:
    #         Ltry=L
    #     else:
    #         Ltry=Lnew[i]
    #     Lnew=splitter(Ltry, sep[i])
    #     if i==len(sep)-1:
    #         Lsplit.append(Lnew)
    #     else:
    #         Lsplit.append(Lnew[i])
    # return Lsplit

print(split_by_num([1,2,3,4,5,2,1], [2,5]))

##guerzhoy
def split_list(L, seps):
    res = []
    cur = []
    for e in L:
        if e not in seps:
            cur.append(e) #current one without e
        else:
            if len(cur)>0: #not empty
                res.append(cur) #once you get e in cur, you move it over to res and then reset cur
                cur = []
    return res

#alternative way: (like my splitter))
def list_replace(L, target, seps):
    res = []
    for e in L:
        if e in seps:
            res.append(target)
        else:
            res.append(e)
    return res


def split_list_like_str(L, seps):
    L1=list_replace(L, seps[0], seps)
    return split_list(L, sep)
