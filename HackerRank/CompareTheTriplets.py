# https://www.hackerrank.com/challenges/compare-the-triplets/problem

a = input()
b = input()

newA = a.split(' ')
newB = b.split(' ')

lstA = [int(num) for num in newA]
lstB = [int(num) for num in newB]

pointA = 0
pointB = 0

length = min(len(lstA), len(lstB))

for i in range(length):
    if lstA[i] > lstB[i]:
        pointA += 1
    elif lstA[i] < lstB[i]:
        pointB += 1

print(pointA, pointB)