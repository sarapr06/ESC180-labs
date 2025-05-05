#question 7
import random
def get_padded_value(x,i): #returns 0 if x[i] dne and returns x[i] otherwsie -- takes out big and small values
    if i<0 or i>=len(x):
        return 0
    else:
        return x[i]
'''def est_vel(x, i): #not using padded value
    est_v_a = (x[i+1] - x[i-1])/0.2
    est_v_b = (x[i+2]-x[i-2])/0.4
    return 0.5*est_v_a+0.4*est_v_b'''
def est_vel(x, i): #not using padded value
    est_v_a = (get_padded_value(x,i+1) - get_padded_value(x,i-1))/0.2
    est_v_b = (get_padded_value(x,i+2) - get_padded_value(x,i-2))/0.4
    return 0.6*est_v_a+0.4*est_v_b
def generate_data():
    data=[0,0,0,0,0]
    #constant velocity of 1m per 0.1s
    #ideal data: [0,1,2,3,4,5,6]
    for i in range(len(data)):
        data[i] = i + 0.1*(random.random()-0.5)
    return data
def experiment():
    sum_errs=0
    for i in range(10000):
        data = generate_data()
        sum_errs +=abs(est_vel(data,4)-10)
    print(sum_errs/10000)
if __name__=='__main__':
    experiment()