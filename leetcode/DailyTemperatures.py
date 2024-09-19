# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)

        return res