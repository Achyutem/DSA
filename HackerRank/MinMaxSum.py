# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
            
    mini = min(arr)
    maxi = max(arr)

    mini_sum = sum(arr) - maxi
    maxi_sum= sum(arr)-mini
    
    print(mini_sum, maxi_sum)