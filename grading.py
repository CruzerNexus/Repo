grade = input("Please enter your score (0-100): ")
grade = int(grade)
if 90 <= grade <= 100:
    finalGrade = "A"
elif 80 <= grade < 90:
    finalGrade = "B"
elif 70 <= grade < 80:
    finalGrade = "C"
elif 60 <= grade < 70:
    finalGrade = "D"
elif 0 <= grade < 60:
    finalGrade = "F"
else:
    finalGrade = "not a valid grade, please try again"
print(f"Your letter grade is {finalGrade}.")
