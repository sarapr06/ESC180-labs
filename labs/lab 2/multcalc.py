#question 6: multiplication:

def display_current_value(x):
    return  x
def mult(to_mult):
    global y
    y=y*to_mult
    return y

if __name__=="__main__":
    x=3
    print(mult(3))
    print("the current value is:")
    print(display_current_value(y))