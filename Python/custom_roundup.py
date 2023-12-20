
'''
Sam is a professor at the university and likes to round each student's  according to these rules:
Rule: 1 If the difference between the grade and the next multiple of 5 is less than 3 , round grade up to the next multiple of 5.
Rule: 2  If the value of  grade is less than 38, no rounding occurs as the result will still be a failing grade.

'''




def customRound(num, grade):
    if num < 3:
        return grade + num
    else:
        return grade

def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    for grade in grades:
        if grade >= 38 and grade % 5 != 0:
            lastDigit = int(list(str(grade))[1])
            if lastDigit > 5:
                diff = 10 - lastDigit
                roundedGrades.append(customRound(diff, grade))
            elif lastDigit < 5:
                diff = 5 - lastDigit
                roundedGrades.append(customRound(diff, grade))
        else:
            roundedGrades.append(grade)
    return roundedGrades


grades = []

for _ in range(5):
        grades_item = int(input().strip())
        grades.append(grades_item)

print(grades)
