# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        arr = sorted(num1 + num2)
        n = len(arr)

        odd = float(arr[n // 2])
        even = (arr[n // 2 - 1] + arr[n // 2]) / 2.0

        if n % 2 == 1:
            return odd
        else:
            return even
