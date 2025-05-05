def display_current_value():
    global y
    print(y)

def add(to_add):
    global y
    y=y+to_add

def mult(to_mult):
    global y
    y=y*to_mult

def div(to_div):
    global y
    y=y/to_div

def memory():
    global mem
    mem = y

def recall():
    global mem
    y = mem
    return y

def undo():
    global y
    global mem
    mem,y=y,mem
    return y

if __name__=="__main__":
    y=0
    memory() #stores y
    display_current_value()
    add(5)
    memory() #stores y
    display_current_value()
    mult(2)
    undo()
    display_current_value()
    undo()
    display_current_value()
    print("the current value for the calculator is:")
    display_current_value()