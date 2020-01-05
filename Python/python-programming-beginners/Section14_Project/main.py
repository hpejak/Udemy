#!/usr/bin/env python3

import functions

students = {"John Wick":780, "John McClane":870,"Martin Riggs":920,"Roger Murtaugh":540,"Stanley Goodspeed":480,"John Patrick Mason":760,"Francis X. Hummel":660,"Cameron Poe":970,"Vince Larkin":580,"Castor Troy":770,"Sean Archer":1000,
"Randall Raines":980,"Sara Wayland":710,"Max Rockatansky":950}

rewards = (500,300,100)


addStudents = input("Do you won't to add new Student? (yes/NO): ")

if (addStudents.lower() == "yes"):
    functions.insertStudents(students)


functions.appreciateStudent(students)

functions.reward(functions.topStudents(students),rewards)
