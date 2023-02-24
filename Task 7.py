#Name:                  Task 7.py
#Author:                Derek Baker
#Date Created:          24-02-2023
#Date Last Modified:    24-02-2023
#
#Purpose:
#
#The purpose of this program is to take the student's information and then prompt the student to enter in the course codes of the programs 
#they want to register for. The program will then display they information and courses they entered.

student = []

firstName = input('Please enter your firstname: ')

lastName = input('Please enter your last name: ')

studentNumber = input('Please enter your student number: ')

student.append(firstName)
student.append(lastName)
student.append(studentNumber)

print(student)