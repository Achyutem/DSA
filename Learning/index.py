#sortin array 
#https://leetcode.com/problems/sort-an-array/


def sortArray(nums):
    if len(nums) <= 1:
        return nums  

    mid = nums[len(nums) // 2]
    left = [x for x in nums if x < mid]  
    middle = [x for x in nums if x == mid]  
    right = [x for x in nums if x > mid]  

    return sortArray(left) + middle + sortArray(right)

nums = [5, 2, 3, 1, 4, 5, 6, 12, 2, 1, 0]
sorted_nums = sortArray(nums)
print(sorted_nums)
