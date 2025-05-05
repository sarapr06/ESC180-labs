#prob 7
def get_days_in_month(y,m):
    if m==1 or m == 3 or m==5 or m == 7 or m == 8 or m == 10 or m==12:
        return 31
    elif m == 2:
        if y%4==0 and y%400!=0:
            return 29
        else:
            return 28
    else:
        return 30
def next_day(y,m,d):
    days_in_month = get_days_in_month(y,m)

    if d<days_in_month:
        d+=1
    else:
        d = 1
        if m == 12:
            m=1
            y+=1
        else:
            m+=1
    print(y,m,d)

def count_days(y1,m1,d1,y2,m2,d2):
    count =0
    y,m,d=y1,m1,d1
    while (y!=y2 or m!=m2 or d!=d2):
        days_in_month = get_days_in_month(y1,m1)
        if d<days_in_month:
            d+=1
        else:
            d = 1
            if m == 12:
                m=1
                y+=1
            else:
                m+=1
        print(y,m,d)
        count+=1
    print("count: " + str(count))

count_days(2005,1,2,2006,2,4)