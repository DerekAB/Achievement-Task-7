#Name:                  Task 7.py
#Author:                Derek Baker
#Date Created:          24-02-2023
#Date Last Modified:    24-02-2023
#
#Purpose:
#
#The purpose of this program is to take the student's information and then prompt the student to enter in the course codes of the programs 
#they want to register for. The program will then display they information and courses they entered.

student = []   #defining the variable as a list

firstName = input('Please enter your firstname: ').capitalize().strip()
student.append(firstName)
#asking for the user's first name and adding it to the list

lastName = input('Please enter your last name: ').capitalize().strip()
student.append(lastName)
#asking for last name and adding to list

studentNumber = int(input('Please enter your student number: '))
student.append(studentNumber)
#asking for student number and adding to list

programList = ['PROG1234', 'INFO4321', 'TECH9876', 'PROG7685'] #defining available courses

print('') #blank space

for n in programList: #printing available courses
    print(n)

print('') #blank space

course = input('Please enter the programs you wish to register '
               'for (put a comma between each code): ').upper().strip()
#asking for the course codes from user and adding to a new list

courseList = course.split(',') #splitting string into list

print('') #adding blank space

print('Student Information: \n')

print(*student, sep='\n') #printing student information

print('') #blank space

print('Registered Courses: \n')

for i in courseList:
    print(i)
#printing course list

