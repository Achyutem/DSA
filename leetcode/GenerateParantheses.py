# https://leetcode.com/problems/generate-parentheses/

"""
so we can only have as many opening parantheses as the number of n
and we are not having a closing parantheses if the number of opening parantheses is lower than the closing parantheses
if open close and n are equal, its the solution
"""


class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
