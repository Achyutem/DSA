class Solution(object):
    def isValidSudoku(self, board):
        def is_valid_group(group):
            seen = set()
            for val in group:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        for row in board:
            check_row = []
            for k in row:
                if k != "." and k in check_row:
                    return False
                check_row.append(k)

        for col in range(len(board)):
            check_col = []
            for row in board:
                value = row[col]
                if value != "." and value in check_col:
                    return False
                check_col.append(value)

        for box_row in range(3):
            for box_col in range(3):
                grid_values = [
                    board[row][col]
                    for row in range(box_row * 3, (box_row + 1) * 3)
                    for col in range(box_col * 3, (box_col + 1) * 3)
                ]
                if not is_valid_group(grid_values):
                    return False

        return True
