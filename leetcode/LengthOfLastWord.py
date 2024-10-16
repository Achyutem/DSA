# https://leetcode.com/problems/length-of-last-word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        n = -1

        while n >= -len(words) and len(words[n]) == 0:
            n -= 1
        return len(words[n])
