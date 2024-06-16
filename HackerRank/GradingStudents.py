# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            remainder = grades[i] % 5
            if remainder >= 3:
                grades[i] += (5 - remainder)
    print(grades)
    return grades

gradingStudents([47, 68, 80])