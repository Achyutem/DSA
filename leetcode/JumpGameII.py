# https://leetcode.com/problems/jump-game-ii


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        target = len(nums) - 1
        current_end = 0
        farthest = 0

        if not nums or len(nums) == 1:
            return 0

        for i in range(target):
            farthest = max(farthest, i + nums[i])

            if i == target:
                return jumps

            if i == current_end:
                jumps += 1
                current_end = farthest

            if current_end >= target:
                return jumps

        return jumps
