# https://leetcode.com/problems/determine-if-two-strings-are-close


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        myset1 = {}
        myset2 = {}

        for i in word1:
            if i in myset1:
                myset1[i] += 1
            else:
                myset1[i] = 1

        for i in word2:
            if i in myset2:
                myset2[i] += 1
            else:
                myset2[i] = 1

        if myset1.keys() != myset2.keys():
            return False

        freq1 = {}
        freq2 = {}

        for j in myset1.values():
            if j in freq1:
                freq1[j] += 1
            else:
                freq1[j] = 1

        for j in myset2.values():
            if j in freq2:
                freq2[j] += 1
            else:
                freq2[j] = 1

        return freq1 == freq2
