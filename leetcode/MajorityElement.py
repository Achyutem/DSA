# https://leetcode.com/problems/majority-element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = {}

        for i in nums:
            if i in arr:
                arr[i] += 1
            else:
                arr[i] = 1

        for key, value in arr.items():
            if value > len(nums) // 2:
                return key
