# https://leetcode.com/problems/sliding-window-maximum


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        dq = collections.deque()
        result = []

        for i in range(len(nums)):
            check = i - k + 1
            if dq and dq[0] < check:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
