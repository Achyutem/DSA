# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l, r = 1, n
        res = r

        while l <= r:
            k = (r + l) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p) / k)

            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
