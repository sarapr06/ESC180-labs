#prob1: while loop for pi

n=1
count=1
i=0
while count<1000:
    if count%2==1 or count == 1:
        i+=(1/n)
    elif count%2==0:
        i-=(1/n)
    n+=2
    count+=1
print(i*4)

#prob2: for loop for pi
n=1
count=1
i=0
for count in range(1, 1000): ## why give negative
    if count%2==1 or count == 1:
        i+=(1/n)
    elif count%2==0:
        i-=(1/n)
    n+=2
    count+=1
print(i*4)


