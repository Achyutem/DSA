# https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for i in operations:
            if i == "+" and len(stack) > 1:
                l = stack.pop()
                k = stack.pop()
                stack.append(k)
                stack.append(l)
                stack.append(l + k)
            elif i == "D":
                l = stack.pop()
                stack.append(l)
                stack.append(l * 2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        for i in stack:
            res += i

        return res


# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         stack = []
#         res = 0

#         for i in operations:
#             if i == '+' and len(stack) > 1:
#                 stack.append(stack[-1] + stack[-2])
#             elif i == 'D':
#                 stack.append(stack[-1]*2)
#             elif i == 'C':
#                 stack.pop()
#             else:
#                 stack.append(int(i))

#         for i in stack:
#             res += i

#         return res
