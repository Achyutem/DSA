# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []
