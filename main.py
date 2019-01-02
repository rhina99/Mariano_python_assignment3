

from students import *          # import the students interface.

# This function is provided as a convenience.
#
def to_letter(grade):
    '''Convert a numeric grade to a letter grade using the prescribed
    formula.'''
    if grade >= 87:
        return 'A'
    elif grade >= 75:
        return 'B'
    elif grade >= 65:
        return 'C'
    else:
        return 'F'


####### ADD ALL SIX REQUIRED FUNCTIONS HERE ##
#
# For example, the command to enter new data will call a function named
# cmd_input(). You need to modify your code from assignment #2 to implement
# that function.




def cmd_input():
    '''Run the command to input new data, and returns that data to the
    _students in student.py file by using class_add() function.'''
    students = class_list()
    while True:
        enter_number = input("\n\nEnter student record (separate fields by commas) or done: ")
        if enter_number == "done":
            break
        else:
            x = enter_number.split()
            y = "".join(x)
            records = y.split(",")
            student_records = tuple(records)
            print(student_records)
            if len(student_records) == 8:
                #Check duplicate
                if class_find_id(student_records[1]) is None:
                    if class_add(student_records[0],student_records[1],student_records[2:]):
                        print("\nRecord Accepted.\n")
                    else:
                        print("\nRecord Failed.\n")
                else:
                    print("\nDuplicate ID(" + student_records[1] + ") number. Record rejected.\n")
            else:
                print("\nRecord incomplete, or record above the limit. Record rejected.\n")



#?
def cmd_average():
    ''' Run the command to print the total class average'''
    class_average()
    if class_average() is None:
        print ("\n\nThere is no input data\n\n")
    else:
        print ("\n\nClass average = " + str(class_average()) + "\n\n")



#?
def cmd_details():
    '''Run the command to print information about a particular student '''
    student_id = input("\n\nEnter the ID of the student: ")
    student = class_find_id(student_id)
    if student_id is None:
        print ("\n\n" + student_id + " ID is not found\n\n")
    else :
        studentGrade = student_grade(student)
        letterGrade = to_letter(studentGrade)
        classAverage = class_average()
        difference  = classAverage - studentGrade
        if difference < 0:
            str_diff = "above"
        elif difference == 0:
            str_diff = "on"
        else:
            str_diff = "below"
        print ("\n\nGrade for " + student[0] + " ID = " + str(student_id) + " : " + str(studentGrade) + " " + letterGrade + " , " + str(abs(difference)) + " points " + str_diff + " average.")




def cmd_listall():
    #Use the class_list() function in your implementation.
    '''Run the command (and function) that will print out a complete list of the student names, IDs, and grades, in alphabetical order by name.'''
    for record in class_list():
        print(student_name(record), str(student_id(record)), str(student_grade(record)), to_letter(student_grade(record)))




def cmd_histogram():
    '''Run the command that will display a “graph” showing the proportions of students with a particular letter grade.'''
    print("Grade distribution for" + str(class_count()) + "students.")
    countA=0
    countB=0
    countC=0
    countF=0
    students = class_list()
    for student in students:
        if student_grade(student) >= 87:
            countA += 1
        elif student_grade(student) >= 75:
            countB += 1
        elif student_grade(student) >= 65:
            countC += 1
        else:
            countF += 1
    print("A", countA, countA * "*")
    print("B", countB, countB * "*")
    print("C", countC, countC * "*")
    print("F", countF, countF * "*")
    
    
    


def print_menu():
    '''Print the menu that oﬀers the user the various command choices. '''
    print('''\n
------------------------------------------------------------------------------
    \n\nWelcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
            1- Enter student records (Name, ID, and 6 marks separated by commas)
            2- Display the class average.
            3- Display the total grade, letter grade and relation to class average for a given student
            4- Display the name, ID, total grade, and letter grade for all students
            5- Display the distribution of grades

            X- Exit
''')
         
    



####### DO NOT CHANGE ANY CODE AFTER THIS LINE!!
# This is the main logic of the program, which is provided for you. 
print("Read", class_read(), "student records.") # Read the test data.
while True:
    print_menu()
    x = input("Select an option by entering its number or X to exit: ").upper()
    if x == '1':
        cmd_input()
    elif x == '2':
        cmd_average()
    elif x == '3':
        cmd_details()
    elif x == '4':
        cmd_listall()           # new command
    elif x == '5':
        cmd_histogram()         # another new command.
    elif x == 'X':              # time to exit.
        break
    else:
        print("Please enter a valid command.")

    
    
    
