# https://leetcode.com/problems/reverse-words-in-a-string


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
        return " ".join(res)
