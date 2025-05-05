def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)
def print_all_energies(w1, w2, w012):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w1, w2, w012))

def lower_or_higher(x0,x1,x2):
    global w01
    global w02
    global w12
    if x0*x1 > 0:
        w01 += 0.1
    else:
        w01 -= 0.1

    if x0*x2 > 0:
        w02 += 0.1
    else:
        w02 -= 0.1

    if x1*x2 > 0:
        w12 += 0.1
    else:
        w12 -= 0.1

    return w01
    return w02
    return w12
def adjust_weight(x0,x1,x2):
    global w01
    global w02
    global w12
    for i in range(12):
        print_all_energies(w01, w02, w12)
        lower_or_higher(x0,x1,x2)
        print("")
        print("===========")



if __name__ == '__main__':
    w01 = 2
    w02 = -1
    w12 = 1
    x0=-1
    x1=1
    x2=1

    adjust_weight(1,-1,1)
