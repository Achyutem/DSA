# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float("inf")

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1

            while lo < hi:
                curr = nums[i] + nums[lo] + nums[hi]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr == target:
                    return curr
                elif curr < target:
                    lo += 1
                else:
                    hi -= 1
        return closest
