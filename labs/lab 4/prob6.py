#prob 7:
import math
def round_sf(k):
    n=1
    count=1
    i=0
    while True:
        if count%2==1 or count == 1:
            i+=(1/n)
        elif count%2==0:
            i-=(1/n)
        n+=2
        count+=1
        print(i*4)
        if round(i*4 ,k)==round(math.pi,k):
            False
            return count
        else:
            True

print(round_sf(1))


