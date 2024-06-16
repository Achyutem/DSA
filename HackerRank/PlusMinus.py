# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    arr_size = len(arr)
    
    positive = []
    negative = []
    zero = []
    
    #condition for type of value in arr
    for i in arr:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)

    print(round(len(positive) / arr_size, 6))
    print(round(len(negative) / arr_size, 6))
    print(round(len(zero) / arr_size, 6)) 