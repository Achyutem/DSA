# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(candles):
    count = 0
    big = max(candles)
    for i in range(len(candles)):
        if(candles[i] == big):
            count += 1
    return count 