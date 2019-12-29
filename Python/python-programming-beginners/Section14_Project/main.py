#!/usr/bin/env python


students = {"John Wick":780, "John McClane":870,"Martin Riggs":920,"Roger Murtaugh":540,"Stanley Goodspeed":480,"John Patrick Mason":760,"Francis X. Hummel":660,"Cameron Poe":970,"Vince Larkin":580,"Castor Troy":770,"Sean Archer":1000,
"Randall Raines":980,"Sara Wayland":710,"Max Rockatansky":950}

rewards = (500,300,100)

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

    print firstStudent,secondStudent,thirdStudent


firstThreeStudents(students)
