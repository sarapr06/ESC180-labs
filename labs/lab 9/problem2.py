import time

#problem 2
def binary_search(L, e):
    low = 0
    it=0
    high = len(L)-1
    while high-low >= 2:
        mid = (low+high)//2 #e.g. 7//2 == 3
        it+=1
        if L[mid] > e:

            high = mid-1
        elif L[mid] < e:

            low = mid+1
        else:
            return (mid, it)
    if L[low] == e:
        return (low, it)
    elif L[high] == e:
        return (high, it)
    else:
        return None, it
#problem a
L=[1,2,3,4,5,6,7,8,9,10]
L1=[30,54,67,78,98,101,304,405,607,809]
#problem b
print(binary_search(L1, 809))


#problem c: can't you just modify the function so that it also returns e if low or high is equal to e

#problem d
L1=[]
L2=[]
L3=[]
L4=[]
for i in range(1, 10000):
    L1.append(i)
for i in range(1, 1000):
    L2.append(i)
for i in range(1, 100):
    L3.append(i)
for i in range(1,10):
    L4.append(i)

print(binary_search(L1, 1))

def linear_search(L,e):
    index=0
    for i in L:
        if i==e:
            return index
        else:
            index+=1
#problem e
def count_time_BS(L, e):
    start = time.time()
    binary_search(L, e)
    end=time.time()
    print(end-start)
def linear_BS(L, e):
    start = time.time()
    linear_search(L,e)
    end=time.time()
    print(end-start)
count_time_BS(L1, 1)
linear_BS(L1,1)

#guerzhoy time function
def timeit(f, inp1, inp2):
    N=500000
    start_t=time.time()
    for i in range(N):
        f(inp1, inp2)
    end_t=time.time()
    return (end_t-start_t)/N
times=[]
#checking for how many iterations it takes for increasing list sizes (guerzhoy)
n_iters_L=[]
length=10
for i in range(7):
    ans, n_iters = binary_search(length*[0], 1)
    n_iters_L.append(n_iters)
    times.append(timeit(binary_search, length*[0], 1))
    length*=10
print(n_iters_L)#increase about 3 each time, because increasing by around log_2(10)~3

print(n_iters)
print(times)
import matplotlib.pyplot as plt
plt.plot(n_iters_L, times)
plt.show()

