# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum():
    length = int(input(''))
    lst = input('')

    newarr = lst.split()
    arr = 0

    for i in range(length):
        arr += int(newarr[i])
    
    return arr

res = simpleArraySum()
print(res)