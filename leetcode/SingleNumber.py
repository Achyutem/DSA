# https://leetcode.com/problems/single-number


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}

        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        for num, count in res.items():
            if count == 1:
                return num

        # XOR Solution
        res = 0
        for n in nums:
            res = n ^ res
        return res
