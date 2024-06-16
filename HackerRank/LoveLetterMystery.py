# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

def theLoveLetterMystery(n):
    pali = n[::-1]
    count = 0
    if n != pali:
        div = len(n) // 2
        for i in range(div):
            if n[i] != pali[i]:
                d = abs(ord(n[i]) - ord(pali[i]))
                count += d
    return count