# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         arr = []
#         max_length = 0
#
#         for i in s:
#             if i in arr:
#                 while arr and arr[0] != i:
#                     arr.pop(0)
#                 arr.pop(0)
#             arr.append(i)
#             max_length = max(max_length, len(arr))
#
#         return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest
