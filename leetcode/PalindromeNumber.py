# https://leetcode.com/problems/palindrome-number


class Solution(object):
    def isPalindrome(self, x):
        y = str(x)[::-1]
        return y == str(x)
