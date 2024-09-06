class Solution:
    def trap(self, heights):
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        leftmax, rightmax = heights[l], heights[r]
        water = 0

        while l < r:
            if heights[l] < heights[r]:
                if heights[l] >= leftmax:
                    leftmax = heights[l]
                else:
                    water += leftmax - heights[l]
                l += 1
            else:
                if heights[r] >= rightmax:
                    rightmax = heights[r]
                else:
                    water += rightmax - heights[r]
                r -= 1

        return water
