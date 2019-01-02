

# This is the list that will hold all of the student records in
# memory. It has an underscore at the beginning because that will
# tend to "hide" from Python's import statement, discouraging programmers
# from manipulating this structure directly.
#
_students = []

# Export the number of grades associated with each student.
#
STUDENT_GRADES = 6
# Export the number of fields expected in a student record. Use this
# value instead of the constant 8 in your main program.
#
STUDENT_FIELDS = STUDENT_GRADES+2

# This function shows a very basic example of reading data from a text
# file. It is provided for you this time. We'll go over the details of
# file I/O soon.
#
def class_read():
    '''Read a class list from a file, storing it in the _students list.'''
    count = 0
    fp = open('class.txt')
    for line in fp:
        if line[0] != '#': # ignore 'comment lines' in the file.
            fields = line.split()
            for i in range(1, len(fields)):
                fields[i] = int(fields[i])
            if class_add(fields[0], fields[1], fields[2:]):
                count += 1
    fp.close()
    return count

def class_add(name, id, grades):
    '''Add a single student record to the internal database.'''
    if len(grades) != STUDENT_GRADES:
        return False
    _students.append((name, id) + tuple(grades))
    return True

####### ADD THE REST OF YOUR FUNCTIONS BELOW THIS LINE.


def class_count():
    '''returns the number of students in the database.'''
    count = len(_students)
    return count


def class_find_id(id):
    ''' returns a student record corresponding to the given ID, if one is present. Returns None if the ID is not found. '''
    for record in _students:
        if str(record[1]) == str(id):
            return record
    return None
#tuple


def class_grades():
    grades = []
    ''' returns a list of the grades for all of the students in the class.'''
    for record in _students:
        grades.append(student_grade(record))
    return grades


def class_average():
    '''returns the mean grade for the class, rounded to an integer. '''
    if class_count() > 0:
        grades = class_grades()
        x = sum(int(grade) for grade in grades)
        average = x / class_count()
        return round(average)
    else:
        return None


def class_list():
    '''returns a list of all of the student records in ascending name order. '''
    _students.sort()
    return _students


def student_grade(record):
    ''' returns, in integer, the grade for an indivdual student, given that student’s record. '''
    marks = record[2:]
    sum_mark = sum(int(mark) for mark in marks)
    return sum_mark


def student_name(record):
    '''returns, in string, the name of a student, given that student’s record.'''
    return record[0]


def student_id(record):
    '''returns, in integer, the ID of a student, given that student’s record.'''
    return int(record[1])









    
