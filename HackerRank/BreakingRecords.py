# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    current_max = current_min = scores[0]
    max = min = 0

    for i in range(1, len(scores)):
        if current_min > scores[i]:
            current_min = scores[i]
            max += 1
        elif current_max < scores[i]:
            current_max = scores[i]
            min += 1
        else:
            pass
    return min, max
