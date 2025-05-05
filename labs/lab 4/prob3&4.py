#prob 4:
i=1
def simplify_fraction(x,y):
    if x > y:
        small = y
    elif x < y:
        small = x
    d = small

    while d >= 1:
        if x % d == 0 and y % d == 0:
            greatest_common_divisor = d
            break
        else:
            d -= 1

    print(str(x/greatest_common_divisor)+"/"+str(y/greatest_common_divisor))

simplify_fraction(4,72)


'''
for i in range(2, greater):
    div = greater/i
    if div == smaller:
        if x>y:
            print(str(x/i) + "/" + str(y/i))
        else:
            print(str(x/i) + "/" + str(y/i))
        break
    else:
        i+=1
print(str(x)+"/" + str(y))
'''