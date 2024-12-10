# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        maxcount = 0
        curr = 0

        for i in range(len(s)):

            if s[i] in vowels:
                curr += 1

            if i >= k:
                if s[i - k] in vowels:
                    curr -= 1

            if i >= k - 1:
                maxcount = max(maxcount, curr)

        return maxcount


# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         vowels = ['a','e','i','o','u']
#         maxcount = 0

#         for i in range(0, len(s)-1 , k):
#             curr = 0
#             if i in vowels:
#                 curr += 1
#             maxcount = max(maxcount, curr)
#         curr = 0

#         return maxcount
