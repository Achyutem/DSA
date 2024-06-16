# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    time = s.split(':')
    if 'P' in s:
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == '12':
            time[0] = '00'
    ntime = ':'.join(time)
    return str(ntime[:-2])