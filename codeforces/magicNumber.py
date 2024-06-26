# https://codeforces.com/problemset/problem/110/A

num = int(input())
 
k = 0
for i in str(num):
    if i == '4' or i == '7':
        k += 1
 
if k== 4 or k == 7:
    print('YES')
else:
    print('NO')
