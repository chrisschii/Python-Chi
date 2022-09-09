print('**** Welcome to the LAB grade calculator! ****')
print()#empty print statement creating space
name = input('Who are we calculating grades for? ==> ')#input for the users name

lab_g = int(input('\nEnter the Labs grade? ==> ')) #takes the input of lab grade
if (lab_g > 100):
    print('The lab value should have been 100 or less.  It has been changed to 100.\n')
    lab_g = 100
elif (lab_g < 0):
    print('The exam value should have been zero or greater. It has been changed to zero')
    lab_g = 0
#this area checks if the lab grade is over 100 or less then 0
    
exam_g = int(input('\nEnter the EXAMS grade? ==> '))
if (exam_g > 100):
    print('The exam value should have been 100 or less.  It has been changed to 100.\n')
    exam_g = 100
elif (exam_g <= 0):
    print('The exam value should have been zero or greater. It has been changed to zero')
    exam_g = 0
#this area checks if the exam grade is over 100 or less then 0
    
attendance_g = int(input('\nEnter the Attendance grade? ==> '))
if (attendance_g > 100):
    print('The attendance value should have been 100 or less.  It has been changed to 100.\n')
    attendance_g = 100
elif (attendance_g < 0):
    print('The attendance value should have been zero or greater. It has been changed to zero')
    attendance_g = 0
print()#empty print statement creating space
#this area checks if the attendance grade is over 100 or less then 0

final_grade = (lab_g * 0.7) + (exam_g * 0.2) + (attendance_g * .1) #the grade of the student is calculated here

if (final_grade >= 90) and (final_grade <= 100):
    grade = 'A'
elif (final_grade >= 80) and (final_grade <= 89):
    grade = 'B'
elif (final_grade >= 70) and (final_grade <= 79):
    grade = 'C'
elif (final_grade >= 60) and (final_grade <= 69):
    grade = 'D'
else:
    grade = 'F'
#this section takes the final grade calculations of the users inputs and compares values to find the letter grade to output    
print(f'The weighted grade for {name} is {final_grade}') #prints the calculated final grade of the three 
print(f'{name} has a letter grade of {grade}') #prints to the user the letter grade.
print() #empty print statement creating space.
print('**** Thanks for using the Lab grade calculator ****')
