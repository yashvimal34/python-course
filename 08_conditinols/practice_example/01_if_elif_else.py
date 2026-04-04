'''
Q1. Write a program that takes a student's score (0-100) and prints their grade:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''

marks_grade = int(input("Enter your marks: "))

if(marks_grade >= 90):
    print("Grade A")

elif (marks_grade >= 80):
    print("Grade B")

elif (marks_grade >= 70):
    print("Grade C")

elif (marks_grade >= 60):
    print("Grade D")

else:
    print("Failed")