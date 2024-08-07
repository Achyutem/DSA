# https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    result = 0
    for i in range(len(s) - m + 1):
        current_sum = 0
        for j in range(m):
            current_sum += s[i + j]
        if current_sum == d:
            result += 1
    return result
