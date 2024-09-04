# https://leetcode.com/problems/group-anagrams/submissions/1376328931/


class Solution(object):
    def groupAnagrams(self, strs):
        GroupAnag = {}

        for s in strs:
            newStr = "".join(sorted(s))

            if newStr not in GroupAnag:
                GroupAnag[newStr] = []

            GroupAnag[newStr].append(s)

        return list(GroupAnag.values())
    
soln = Solution()
strs = ['ant', 'tan', 'bat', 'tab', 'cat']
soln.groupAnagrams(strs)
