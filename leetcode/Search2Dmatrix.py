# https://leetcode.com/problems/search-a-2d-matrix


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l, r = 0, (col * row) - 1

        while l <= r:
            m = (l + r) // 2
            i = m // col
            j = m % col

            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = m - 1
            else:
                l = m + 1

        return False
