# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        res = sorted(nums)

        count = 1
        maxcount = 1
        for i in range(len(res) - 1):
            if res[i + 1] - res[i] == 0:
                count = count
            elif res[i + 1] - res[i] == 1:
                count += 1
            else:
                if count > maxcount:
                    maxcount = count
                count = 1

        if count > maxcount:
            maxcount = count

        return maxcount
