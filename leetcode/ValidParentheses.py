# https://leetcode.com/problems/valid-parentheses/description/


class Solution(object):
    def isValid(self, s):
        # define a stack and a hashmap to match the parantheses
        stack = []
        openToClose = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # if its a closing parantheses, then
            if c in openToClose:
                if stack and stack[-1] == openToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
