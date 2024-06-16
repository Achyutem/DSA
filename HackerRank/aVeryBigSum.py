# https://www.hackerrank.com/challenges/a-very-big-sum/problem

a = int(input())
b = input()

arr = b.split(' ')

lstArr = [int(num) for num in arr]

if len(lstArr) == a:
    sum = 0
    for i in lstArr:
        sum += i
    print(sum)