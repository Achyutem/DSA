# https://leetcode.com/problems/ransom-note


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        b = {}

        for i in ransomNote:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        for i in magazine:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1

        for char in a:
            if char not in b or b[char] < a[char]:
                return False

        return True
