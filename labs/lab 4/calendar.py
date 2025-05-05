def next_day(d,m,y):
    total_days = total_days(m,y)
    if d==31 and m==12:
        y+=1
        m=1
        d=1
    if d==total_days:
        m+=1
        d=1
    else:
        d+=1
    print('y: '+ y + ", m: " + m + ", d: " + d)

def total_days(m,y):
    if m=='1' or m=='3' or m == '5' or m == '7' or m == '8' or m == '10' or m == '12':
        return 31
    elif m == '2':
        if y%4 == 0 and y%400 == 0:
            return 29
        else:
            return 28
    else:
        return 30

def print_days(d1,m1,y1,d2,m2,y2):
    count = 0
    while d1!=d2 or m1!=m2 or y1!=y2:
        total_days1 = total_days(m1,y1)
        if d1==31 and m1==12:
            y1+=1
            m1=1
            d1=1
        if d1==total_days1:
            m1+=1
            d1=1
        else:
            d1+=1
        print('y: '+ str(y1) + ", m: " + str(m1) + ", d: " + str(d1))
        count +=1
    return count

print(print_days(1,1,2006,1,2,2006))