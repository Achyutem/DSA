# https://leetcode.com/problems/product-of-array-except-self/


class Solution(object):
    def productExceptSelf(self, nums):
        count = 1
        zcount = 0
        for i in nums:
            if i != 0:
                count *= i
            else:
                zcount += 1

        result = []

        if zcount > 1:
            return [0] * len(nums)
        else:
            for i in nums:
                if zcount == 0:
                    result.append(count // i)
                elif i == 0:
                    result.append(count)
                else:
                    result.append(0)
        return result
