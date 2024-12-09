# https://leetcode.com/problems/max-number-of-k-sum-pairs


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0

        if len(nums) <= 1:
            return count

        while l < r:
            curr = nums[l] + nums[r]

            if curr == k:
                count += 1
                l += 1
                r -= 1
            elif curr < k:
                l += 1
            else:
                r -= 1

        return count
