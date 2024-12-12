# https://leetcode.com/problems/max-consecutive-ones-iii


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = 0
        zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            newWindow = (r - l) + 1

            window = max(newWindow, window)

        return window
