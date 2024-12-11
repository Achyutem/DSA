# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1
        for i in reversed(range(len(arr))):
            newMax = max(arr[i], currMax)
            arr[i] = currMax
            currMax = newMax
        return arr
