# https://leetcode.com/problems/contains-duplicate/

# Solution 1 using sets


class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()

        for i in nums:
            if i in arr:
                return True
            else:
                arr.add(i)
        return False


# Solutin 2 using list


class Solution(object):
    def containsDuplicate(self, nums):
        arr = []

        for i in nums:
            if i in arr:
                return True
            else:
                arr.append(i)
        return False
