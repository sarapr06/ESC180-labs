#question 1
def my_sqrt(x):
    sqr = x**.5
    return sqr

def my_print_square(x):
    print(x**0.5) #when called, it actually prints. when the other one is called, it does not print unless you say to print the function

if __name__ == "__main__":
    res = my_sqrt(25)
   # print(sqr) #does not work bc it's a local variable -- not defined outside the function'
    res = my_print_square(25)
    print(res) #prints 5.0 then none because it prints the sqr root of 5 but also executes the function and because the function returns nothing, it will also return nothing

#question 2: trace
#basically make a red dot and run "execute selection and advance"

