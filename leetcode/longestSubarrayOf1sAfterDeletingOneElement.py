# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLen = 0
        zeros = 0
        l = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            maxLen = max(maxLen, r - l)

        return maxLen
