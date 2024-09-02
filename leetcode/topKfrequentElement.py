# https://leetcode.com/problems/top-k-frequent-elements/


class Solution(object):
    def topKFrequent(self, nums, k):
        freqArr = {}

        for i in nums:
            if i in freqArr:
                freqArr[i] += 1
            else:
                freqArr[i] = 1

        newLi = []
        newArr = sorted(freqArr, key=freqArr.get, reverse=True)
        print(newArr)
        for i in newArr:
            if len(newLi) < k:
                newLi.append(i)

        return newLi
