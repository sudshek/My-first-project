var  = raw_input("Which file do you want to open")
if var == "student_becomes_teacher.py":
    import student_becomes_teacher
elif var == "battle_ship.py":
    import battle_ship
elif var == "exam-stastistics":
    import exam_stastistics
else :
    print "Wrong input!! No such file exists!!"
