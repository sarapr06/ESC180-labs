#prob 1-3
def find_99(L):
    for i in range(len(L)):
        if L[i][1]==99:
            print(L[i][1])
            break
def get_nums(L):
    nums = []
    for i in range(len(L)):
        nums.append(L[i][1])
    print(nums)
def lookup(L, num):
    for i in range(len(L)):
        if L[i][1]==99:
            print(L[i][0])
            break
    return None
if __name__=='__main__':
    L=[["CIV",92],
        ["180", 98],
        ["103", 98],
        ["194", 95]]

    print(find_99(L))
    get_nums(L)
