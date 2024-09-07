#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        arr = []
        max_length = 0

        for i in s:
            if i in arr:
                while arr and arr[0] != i:
                    arr.pop(0)
                arr.pop(0)
            arr.append(i)
            max_length = max(max_length, len(arr))

        return max_length


soln = Solution()
s = "abcabcbb"
print(soln.lengthOfLongestSubstring(s))
