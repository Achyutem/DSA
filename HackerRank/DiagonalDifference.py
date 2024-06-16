# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    arr_size = len(arr)

    #left to right
    left_to_right = 0
    i = 0
    exit = True
    while exit:
        left_to_right = left_to_right + arr[i][i]
        i += 1
        if i == arr_size:
            exit = False

    #right to left
    right_to_left = 0
    i = 0
    j = arr_size - 1
    exit = True
    while exit:
        right_to_left = right_to_left + arr[i][j]
        i += 1
        j -= 1
        if i == arr_size:
            exit = False

    #difference calculate
    return abs(left_to_right - right_to_left)