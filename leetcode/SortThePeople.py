# https://leetcode.com/problems/sort-the-people/


class Solution(object):
    def sortPeople(self, names, heights):
        newList = []

        for i in range(len(names)):
            name = names[i]
            height = heights[i]
            newList.append((name, height))

        sortedPeople = sorted(newList, key=lambda x: x[1], reverse=True)

        sortedName = [name for name, height in sortedPeople]
        return sortedName

        sortedHeight = sorted(newList, key=newList.get, reverse=True)

        return sortedHeight
