# https://leetcode.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, heights):
        maxarea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r - l)
                l += 1
            else:
                area = heights[r] * (r - l)
                r -= 1

            if area > maxarea:
                maxarea = area

        return maxarea
