#problem 4d

def initialize():
    global knols
    global time
    global last_coffee
    global coffee_count
    global coffee_time
    global coffee_prevtime
    global overtime_fr
    overtime_fr = False
    coffee_prevtime = 1000000
    coffee_time = 0
    coffee_count = 0
    last_coffee = False
    current_time = 0
    knols = 0
    time = 0
def drink_coffee(): # your code here
    global coffee_time
    global coffee
    global last_activity
    global last_coffee
    global coffee_count
    global coffee_time
    global TimeoutError
    global coffee_prevtime
    global overtime_fr
    last_coffee = True
    if (abs(time-coffee_prevtime) <= 20) and last_coffee == True:
        overtime_fr = True
    coffee_time, coffee_prevtime = time, coffee_time
    coffee_count+=1
def study(minutes): # your code here
    global time
    time += minutes
    global knols
    global last_time
    global last_coffee
    global coffee_time
    global coffee_time
    global coffee_count
    global coffee_prevtime
    global overtime_fr
    if overtime_fr:
        return knols
    elif last_coffee == True:
        knols = knols + minutes*10
        last_coffee = False
        return knols
    elif last_coffee == False:
        knols = knols + minutes*5


#5 knols per minute of study if have not drunk coffee right before study session
#10 knols per min of study if had coffee right before session
#if more than 2 cups of coffee over 2h, 0 knoles per hour from there on

if __name__=="__main__":
    initialize() # start the simulation
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols)
    drink_coffee() # knols = 400
    study(10) # knols = 500
    print(knols)
    drink_coffee() # knols = 500
    study(10) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600
    print(knols)