def firstThreeStudents(students):
    firstStudent = None
    secondStudent = None
    thirdStudent = None

    for student in students:
        if not firstStudent:
            firstStudent = student
        if not secondStudent:
            secondStudent = student
        if not thirdStudent:
            thirdStudent = student

        if students[student] > students[firstStudent]:
            if students[firstStudent] > students[secondStudent]:
                if students[secondStudent] > students[thirdStudent]:
                    thirdStudent = secondStudent
                secondStudent = firstStudent
            firstStudent = student
        elif students[student] > students[secondStudent]:
            if students[secondStudent] > students[thirdStudent]:
                thirdStudent = secondStudent
            secondStudent = student
        elif students[student] > students[thirdStudent]:
            thirdStudent = student

    print (firstStudent,secondStudent,thirdStudent)


def topStudents(students):
    students_sor = sorted(students.items(), key=lambda kv: kv[1], reverse = True)
    topThree = [students_sor[0],students_sor[1],students_sor[2]]
    return topThree


def insertStudents(students):
    numForInsert = int(input("How many students you will be entering: "))

    for student in range(0, numForInsert):
        studentName = input("Enter full name of Student: ")
        studentMarks = int(input("Enter Marsks of Student: "))

        students[studentName ] = studentMarks

    return students


def reward(topStudents,rewards):
    try:
        print ("{} has received firs price ${}, for scoring {} marks ".format(topStudents[0][0], rewards[0],topStudents[0][1]))
        print ("{} has received second price ${}, for scoring {} marks ".format(topStudents[1][0], rewards[1],topStudents[1][1]))
        print ("{} has received third price ${}, for scoring {} marks ".format(topStudents[2][0], rewards[2],topStudents[2][1]))
    except IndexError:
        print ("There is no 3 students for rewarding")

def appreciateStudent(students):
    for student in students:
        if students[student] > 950:
            print ("Special congratulation to {} for scoring more marks then upper threshold".format(student))
