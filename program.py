'''
Name: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import os

def get_menu():
    return "Main Menu\nChoose any of these options:\n1. Add a course\n2. Add a student \n\
3. Add a teacher\n4. List all students\n5. List all teachers \n6. Search for a student by \
their name or student ID\n7. List the teachers and their courses for a student\n8. Show the \
GPA of a course\nEnter zero to exit the program."


def is_valid_credit_hour(chour: str) -> bool:
    try:
        chour = int(chour)
        if chour >= 1 and chour <= 5:
            return 1
    except:
        return 0


def add_course():
    # Boolean indicating valid course code
    valid_code = False

    while not valid_code:
        # Prompt user for course code
        ccode = input("Enter the course code: ")

        # Check if length of course code is 6
        if len(ccode) != 6:
            print("The length of course codes entered should be 6.")
            continue

        # If course_info.txt exists
        if os.path.isfile("course_info.txt"):
            # Check if course code already exists in file
            with open("course_info.txt", 'r') as cfile:
                for i in cfile.readlines():
                    if i.lower().split(',')[0] == ccode.lower():
                        print("This course code exists in our database.")
                        valid_code = False
                        break
                    else:
                        valid_code = True

            # If course valid and not in file then open file in append mode
            if valid_code:
                cfile = open("course_info.txt", 'a')
        # If course_info.txt doesn't exist, open it in write mode (thereby creating it)
        else:
            cfile = open("course_info.txt", 'w')

    # Boolean indicating valid course name
    valid_name = False

    while not valid_name:
        # Prompt user for course name
        cname = input("Enter the course name: ").strip()

        # If sname is not between 1 and 40
        if len(cname) < 1 or len(cname) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue

        # Boolean for alpha
        is_alpha = True

        # Check if name is alpha (account for spaces)
        for i in cname.split(' '):
            if not i.isalpha() and i != ' ':
                print("The name should be alphabetic.")
                valid_name = False
                is_alpha = False
                break

        # If valid exit while loop
        if is_alpha:
            valid_name = True

    while True:
        # Prompt user for course credit hours
        chour = input("How many credit hours does this course have? ")

        # Check if credit hour is not between 1 and 5 inclusive
        if not is_valid_credit_hour(chour):
            print("The credit hour for each course should be an integer between 1 and 5 inclusive.")
        # If else is valid, exit while loop
        else:
            break
            
    # Put together course details
    course = f"{ccode},{cname},{chour}\n"
    
    cfile.write(course)
    cfile.close()


def add_student():
    # Boolean indicating valid student ID
    valid_id = False

    while not valid_id:
        # Prompt user for student ID
        sid = input("Enter the student ID: ")

        # Check if length student ID is 10
        if len(sid) != 10:
            print("The length of the student ID should be 10 characters.")
            continue

        # If student_info.txt exists
        if os.path.isfile("student_info.txt"):
            # Check if sid exists in file
            with open("student_info.txt", 'r') as sfile:
                # Check if file is empty
                if os.path.getsize("student_info.txt") == 0:
                    break
                for i in sfile.readlines():
                    if i.split(',')[0] == sid:
                        valid_id = False
                        print("This student ID exists in our database.")
                        break
                    else:
                        valid_id = True
        else:
            valid_id = True   

    # Boolean indicating valid student name
    valid_name = False

    while not valid_name:
        # Prompt user for student name
        sname = input("Enter the student name: ").strip().lower().title()

        # If sname is not between 1 and 40
        if len(sname) < 1 or len(sname) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue

        # Boolean for alpha
        is_alpha = True

        # Check if name is alpha (account for spaces)
        for i in sname.split(' '):
            if not i.isalpha() and i != ' ':
                print("The name should be alphabetic.")
                valid_name = False
                is_alpha = False
                break

        # If valid exit while loop
        if is_alpha:
            valid_name = True

    while True:
        # Prompt user for program code
        pcode = input("Enter the program code: ")

        if len(pcode) != 5:
            print("The length of the program code entered should be 5.")
        else:
            break   

    while True:
        # Prompt user for no. of courses student has
        ncourses = input("How many courses does this student have? ")

        try:
            ncourses = int(ncourses) 
            # If ncourses is not between 1 and 5
            if ncourses < 1 or ncourses > 5:
                print("You can enter a number between 1 to 5.")
            # Else if valid number of courses, exit while loop
            else:
                break
        # If ncourses is not an integer
        except:
            print("Number of courses should be an integer value.")


    # Create string to add student info
    student_info = ""
    student_info += f"{sid},{sname.title()},{pcode.upper()}"

    for code in range(1, ncourses+1):
        # Boolean indicating valid course code
        valid_code = False

        while not valid_code:
            # Prompt user for 1st course code
            ccode = input(f"Enter course code {code}: ")

            # Check if length of course code is 6
            if len(ccode) != 6:
                print("The length of course codes entered should be 6.")
                continue

            # If course_info.txt exists
            if os.path.isfile("course_info.txt"):
                # Check if course code exists in file
                with open("course_info.txt", 'r') as cfile:
                    for i in cfile.readlines():
                        if i.lower().split(',')[0] == ccode.lower():
                            valid_code = True
                            break
                # If not valid, print message
                if not valid_code:
                    print("This course does not exist in our database.")
    
        while True:
            # Prompt user for course score
            score = input("Enter the student's score for this course: ")

            try:
                score = float(score) 
                # If score is not between 0 and 100
                if score < 0 or score > 100:
                    print("The score for each course should be in the range of 0 to 100.")
                # Else if valid score, exit while loop
                else:
                    break
            # If score is not a digit
            except:
                print("Score should be a float value.")
        
        # Add info to student_info string
        student_info += f",{ccode.upper()}:{score}"

    # Add info to student file
    with open('student_info.txt', 'a') as sfile:
        sfile.write(student_info)
                

def add_teacher():
    # Boolean indicating valid staff ID
    valid_id = False

    while not valid_id:
        # Prompt user for staff ID
        tid = input("Enter the staff ID: ")

        # Check if length staff ID is 7
        if len(tid) != 7:
            print("The length of the staff ID should be 7 characters.")
            continue

        # If teacher_info.txt exists
        if os.path.isfile("teacher_info.txt"):
            # Check if tid exists in file
            with open("teacher_info.txt", 'r') as tfile:
                # Check if file is empty
                if os.path.getsize("teacher_info.txt") == 0:
                    break
                for i in tfile.readlines():
                    if i.split(',')[0] == tid:
                        valid_id = False
                        print("This teacher ID exists in our database.")
                        break
                    else:
                        valid_id = True
        else:
            valid_id = True   

    # Boolean indicating valid student name
    valid_name = False

    while not valid_name:
        # Prompt user for teacher name
        tname = input("Enter the teacher name: ").strip().lower().title()

        # If tname is not between 1 and 40
        if len(tname) < 1 or len(tname) > 40:
            print("The length of the name should be between 1 and 40 characters inclusive.")
            continue

        # Boolean for alpha
        is_alpha = True

        # Check if name is alpha (account for spaces)
        for i in tname.split(' '):
            if not i.isalpha() and i != ' ':
                print("The name should be alphabetic.")
                valid_name = False
                is_alpha = False
                break

        # If valid exit while loop
        if is_alpha:
            valid_name = True

    while True:
        # Prompt user for no. of courses teacher teaches
        ncourses = input("How many courses does this teacher teach? ")

        try:
            ncourses = int(ncourses) 
            # If ncourses is not between 1 and 5
            if ncourses < 1 or ncourses > 5:
                print("You can enter a number between 1 to 5.")
            # Else if valid number of courses, exit while loop
            else:
                break
        # If ncourses is not an integer
        except:
            print("Number of courses should be an integer value.")

    # Create string to add teacher info
    teacher_info = ""
    teacher_info += f"{tid},{tname.title()}"

    # Create list to check for duplicate course codes
    course_list = []

    for code in range(1, ncourses+1):
        # Boolean indicating valid course code
        valid_code = False

        while not valid_code:
            # Prompt user for 1st course code
            ccode = input(f"Enter course code {code}: ")

            # Check if length of course code is 6
            if len(ccode) != 6:
                print("The length of course codes entered should be 6.")
                continue
            elif ccode in course_list:
                print("This course has been entered before.")
                continue

            # If course_info.txt exists
            if os.path.isfile("course_info.txt"):
                # Check if course code exists in file
                with open("course_info.txt", 'r') as cfile:
                    for i in cfile.readlines():
                        if i.lower().split(',')[0] == ccode.lower():
                            valid_code = True
                            course_list.append(ccode)
                            break
                # If not valid, print message
                if not valid_code:
                    print("This course does not exist in our database.")
        
        # Add info to teacher_info string
        teacher_info += f",{ccode.upper()}"

    # Add info to teacher file
    with open('teacher_info.txt', 'a') as tfile:
        tfile.write(teacher_info)

def student_gpa(ls = []) -> float:
    if ls == []:
        # Create file object for student info file and its store contents in a list
        with open('student_info.txt', 'r') as sfile:
            student_list = sfile.readlines()

        # Create a list to store gpas
        gpa_list = []

        # Retrieve course codes and their scores
        for i in student_list:
            # Split elements of the string (remove newline character)
            stu_list = i.strip('\n').split(',')
            sid = stu_list[0]
            sname = stu_list[1]
            pcode = stu_list[2]

            # Create a list to store student course codes and scores
            ls = []

            # Fill in the list (ls)
            for j in range(3, len(stu_list)):
                temp = stu_list[j].split(':')
                ls.append((temp[0], temp[1]))

            # Recursive call to student_gpa to retrieve gpa
            gpa_list.append(student_gpa(ls))
        
        return gpa_list

    else:
        # Create file object for course info file and its store contents in a list
        with open('course_info.txt', 'r') as cfile:
            course_list = cfile.readlines()

        # Create a list to store credit hours
        chours = []
        # Create a list to store the values of grades multiplied by their respected credit hours
        grade_hours = []

        # Fill in the lists above
        for i in ls:
            # Find grade using student's mark from ls
            if int(float(i[1])) >= 80 and int(float(i[1])) <= 100:
                grade = 4.00
            elif int(float(i[1])) >= 75 and int(float(i[1])) < 80:
                grade = 3.67
            elif int(float(i[1])) >= 70 and int(float(i[1])) < 75:
                grade = 3.33
            elif int(float(i[1])) >= 65 and int(float(i[1])) < 75:
                grade = 3.00
            elif int(float(i[1])) >= 60 and int(float(i[1])) < 65:
                grade = 2.67
            elif int(float(i[1])) >= 55 and int(float(i[1])) < 60:
                grade = 2.33
            elif int(float(i[1])) >= 50 and int(float(i[1])) < 55:
                grade = 2.00
            elif int(float(i[1])) >= 47 and int(float(i[1])) < 50:
                grade = 1.67
            elif int(float(i[1])) >= 44 and int(float(i[1])) < 47:
                grade = 1.33
            elif int(float(i[1])) >= 40 and int(float(i[1])) < 44:
                grade = 1.00
            else:
                grade = 0.00

            for j in course_list:
                # Split elements of the string (remove newline character)
                temp = j.strip('\n').split(',')
                # Locate same course code and retrieve credit hour
                if i[0] == temp[0]:
                    chours.append(int(temp[2]))
                    grade_hours.append(grade*int(temp[2]))
                    break

        # Calculate gpa
        gpa = sum(grade_hours) / sum(chours)

        return gpa
        

def list_students():
    # Create file object for student info file and its store contents in a list
    with open('student_info.txt', 'r') as sfile:
        student_list = sfile.readlines()

    # Retrieve student gpas
    gpa = student_gpa()

    # Retrieve student info
    for i in range(len(student_list)):
        # Split elements of the string (remove newline character)
        stu_list = student_list[i].strip('\n').split(',')
        sid = stu_list[0]
        sname = stu_list[1]
        pcode = stu_list[2]

        # Create a list to store student course codes and scores
        ls = []

        # Fill in the list (ls)
        for j in range(3, len(stu_list)):
            temp = stu_list[j].split(':')
            ls.append((temp[0], temp[1]))

        # Retrieve credit hours
        with open('course_info.txt', 'r') as cfile:
            course_list = cfile.readlines()

        # Create a list to store credit hours
        chours = []
        
        for j in ls:
            for k in course_list:
                # Split elements of the string (remove newline character)
                temp = k.strip('\n').split(',')
                # Locate same course code and retrieve credit hour
                if j[0] == temp[0]:
                    chours.append(int(temp[2]))
                    break

        # Display results
        print(f"Student ID: {sid}")
        print(f"Student Name: {sname}")
        print(f"Program Code: {pcode}")
        print("Course    Credit Hour    Score")
        for j in range(len(ls)):
            print(f"{ls[j][0]}         {chours[j]}           {float(ls[j][1])}")
        print("GPA is %.2f\n" % gpa[i])


def list_teachers():
    with open('teacher_info.txt', 'r') as tfile:
        teacher_list = tfile.readlines()

    # Retrieve student info
    for i in range(len(teacher_list)):
        # Split elements of the string (remove newline character)
        tea_list = teacher_list[i].strip('\n').split(',')
        tid = tea_list[0]
        tname = tea_list[1]

        # Retrieve contents of course info file
        with open('course_info.txt', 'r') as cfile:
            course_list = cfile.readlines()

        # Create a list to store teacher course codes and their names
        ls = []

        # Fill in the list (ls)
        for j in range(2, len(tea_list)):
            #temp = tea_list[j].split(':')
            for k in course_list:
                course_info = k.split(',')
                if tea_list[j] == course_info[0]:
                    ls.append((tea_list[j], course_info[1]))

        # Display results
        print(f"Staff ID: {tid}")
        print(f"Teacher Name: {tname}")
        print("Teaches the following courses:")
        for j in ls:
            print(f"{j[0]}: {j[1]}")
        print()


def search_student():
    print("Search students based on: ")
    print("Select 1 for ID")
    print("Select 2 for Name")
    
    option = input("Enter your choice: ")

    if option == '1':
        # Boolean indicating valid student ID
        valid_id = False

        while not valid_id:
            # Prompt user for student ID
            sid = input("Enter student ID: ")

            # Check if length student ID is 10
            if len(sid) != 10:
                print("The length of the student ID should be 10 characters.")
                continue

            # Create a list to store student course codes and scores
            ls = []

            # If student_info.txt exists
            if os.path.isfile("student_info.txt"):
                # Check if sid exists in file
                with open("student_info.txt", 'r') as sfile:
                    # Check if file is empty
                    if os.path.getsize("student_info.txt") == 0:
                        break
                    for i in sfile.readlines():
                        temp = i.strip('\n').split(',')
                        
                        # Check if sid is on this line in the file. If so, retrieve info
                        if temp[0] == sid:
                            valid_id = True
                            sname = temp[1]
                            pcode = temp[2]

                            # Fill in the list (ls) with course codes and scores
                            for j in range(3, len(temp)):
                                temp2 = temp[j].split(':')
                                ls.append((temp2[0], temp2[1]))

                            break

            # If sid not found                            
            if not valid_id:
                print("This student ID/name does not exist in our database.")
                continue
                        
            # Retrieve credit hours
            with open('course_info.txt', 'r') as cfile:
                course_list = cfile.readlines()

            # Create a list to store credit hours
            chours = []

            for j in ls:
                for k in course_list:
                    # Split elements of the string (remove newline character)
                    temp = k.strip('\n').split(',')
                    # Locate same course code and retrieve credit hour
                    if j[0] == temp[0]:
                        chours.append(int(temp[2]))
                        break
            
            # Retrieve gpa
            gpa = student_gpa(ls)

            # Display results
            print(f"Student ID: {sid}")
            print(f"Student Name: {sname}")
            print(f"Program Code: {pcode}")
            print("Course    Credit Hour    Score")
            for j in range(len(ls)):
                print(f"{ls[j][0]}         {chours[j]}          {float(ls[j][1])}")
            print("GPA is %.2f" % gpa)

    elif option == '2':
        # Boolean indicating valid student name
        valid_name = False

        while not valid_name:
            # Prompt user for student name
            sname = input("Enter the student name: ").strip().lower().title()

            # If sname is not between 1 and 40
            if len(sname) < 1 or len(sname) > 40:
                print("The length of the name should be between 1 and 40 characters inclusive.")
                continue

            # Boolean for alpha check
            is_alpha = True

            # Check if name is alpha (account for spaces)
            for i in sname.split(' '):
                if not i.isalpha() and i != ' ':
                    print("The name should be alphabetic.")
                    is_alpha = False
                    break

            # If name not alphabetic, give user another try
            if not is_alpha:
                continue

            # Create a list to store student course codes and scores
            ls = []

            # If student_info.txt exists
            if os.path.isfile("student_info.txt"):
                # Check if sid exists in file
                with open("student_info.txt", 'r') as sfile:
                    # Check if file is empty
                    if os.path.getsize("student_info.txt") == 0:
                        break
                    for i in sfile.readlines():
                        temp = i.strip('\n').split(',')
                        
                        # Check if student name is  line in file. If so, retrieve info
                        if temp[1] == sname:
                            valid_name = True
                            sid = temp[0]
                            pcode = temp[2]

                            # Fill in the list (ls) with course codes and scores
                            for j in range(3, len(temp)):
                                temp2 = temp[j].split(':')
                                ls.append((temp2[0], temp2[1]))

                            break

            # If student name not found                            
            if not valid_name:
                print("This student ID/name does not exist in our database.")
                continue
                        
            # Retrieve credit hours
            with open('course_info.txt', 'r') as cfile:
                course_list = cfile.readlines()

            # Create a list to store credit hours
            chours = []

            for j in ls:
                for k in course_list:
                    # Split elements of the string (remove newline character)
                    temp = k.strip('\n').split(',')
                    # Locate same course code and retrieve credit hour
                    if j[0] == temp[0]:
                        chours.append(int(temp[2]))
                        break
            
            # Retrieve gpa
            gpa = student_gpa(ls)

            # Display results
            print(f"Student ID: {sid}")
            print(f"Student Name: {sname}")
            print(f"Program Code: {pcode}")
            print("Course    Credit Hour    Score")
            for j in range(len(ls)):
                print(f"{ls[j][0]}         {chours[j]}          {float(ls[j][1])}")
            print("GPA is %.2f" % gpa)
    else:
        print("Wrong menu selection.")


def list_teachers_courses():
    # Boolean indicating valid student ID
    valid_id = False

    while not valid_id:
        # Prompt user for student ID
        sid = input("Enter student ID: ")

        # Check if length student ID is 10
        if len(sid) != 10:
            print("The length of the student ID should be 10 characters.")
            continue

        # Create a list to store course codes
        course_codes = []

        # If student_info.txt exists
        if os.path.isfile("student_info.txt"):
            # Check if sid exists in file
            with open("student_info.txt", 'r') as sfile:
                # Check if file is empty
                if os.path.getsize("student_info.txt") == 0:
                    break
                for i in sfile.readlines():
                    temp = i.strip('\n').split(',')
                        
                    # Check if sid is on this line in the file. If so, retrieve info
                    if temp[0] == sid:
                        valid_id = True

                        # Fill in the list (ls) with course codes
                        for j in range(3, len(temp)):
                            temp2 = temp[j].split(':')
                            course_codes.append((temp2[0]))

                        break

        # If sid not found                            
        if not valid_id:
            print("This student ID does not exist in our database.")
            continue 

        with open('course_info.txt', 'r') as cfile:
            course_list = cfile.readlines()

        # List to store tuples containing course codes and their course names
        codes_names = []

        # Retrieve course names
        for i in course_codes:
            for j in course_list:
                temp = j.strip('\n').split(',')

                if i == temp[0]:
                    codes_names.append((i,temp[1]))
                    break

        with open('teacher_info.txt', 'r') as tfile:
            teacher_list = tfile.readlines()

        # List to store tuples of teacher and course names
        teacher_course = []

        # Retrieve teacher names and populate teacher_course list
        for i in codes_names:
            for j in teacher_list:
                temp = j.strip('\n').split(',')

                for k in range(2, len(temp)):
                    if i[0] == temp[k]:
                        teacher_course.append((temp[1], i[1]))

        # Display the information
        for i in teacher_course:
            print(f"Teacher Name: {i[0]}")
            print(f"Course Name: {i[1]}\n")


def course_gpa():
    # Boolean indicating valid course code
    invalid_code = True

    while invalid_code:
        # Prompt user for course code
        ccode = input("Enter the course code: ").upper()

        # Check if length of course code is 6
        if len(ccode) != 6:
            print("The length of course codes entered should be 6.")
            continue

        # If course_info.txt exists
        if os.path.isfile("course_info.txt"):
            # Check if course code already exists in file
            with open("course_info.txt", 'r') as cfile:
                for i in cfile.readlines():
                    if i.split(',')[0] == ccode:
                        invalid_code = False
                        break
        
        # If code not found in file
        if invalid_code:
            print("This course code does not exist in our database.")

    # Create a list to store tuples of student marks with the respected course code
    student_marks = []

    with open('student_info.txt', 'r') as sfile:
        student_list = sfile.readlines()

    # Retrieve student marks
    for i in student_list:
        # Check if this student has the course code
        if ccode in i:
            temp = i.strip('\n').split(',')

            # Remove sid, student name and program code
            for j in range(3):
                temp.remove(temp[0])
            
            # Populate student_list with tuples: (course code, mark)
            for j in temp:
                if ccode in j:
                    student_marks.append((ccode, j.split(':')[1]))
                    break
    
    # Calculate the gpa
    gpa = student_gpa(student_marks)
    
    print(f"GPA for this course is %.2f" % gpa)


def main():
    while True:
        # Print menu
        print(get_menu())

        # Prompt user for menu option
        option = input("Enter your choice: ") 
 
        # If 0: Exit program
        if option == '0':
            print("Exiting the program...")
            exit(0)
        # If 1: Add a course
        elif option == '1':
            add_course()
        # If 2: Add a student
        elif option == '2':
            add_student()
        # If 3: Add a teacher
        elif option == '3':
            add_teacher()
        # If 4: List all students
        elif option == '4':
            list_students()
            continue # to avoid newline from print() below
        # If 5: List all teachers
        elif option == '5':
            list_teachers()
            continue # to avoid newline from print() below
        # If 6: Search for a student
        elif option == '6':
            search_student()
        # If 7: List the teachers and their courses
        elif option == '7':
            list_teachers_courses()
            continue # to avoid newline from print() below
        # If 8: Show the GPA of a course
        elif option == '8':
            course_gpa()
        else:
            print("Wrong menu selection")

        # Print newline before displaying the menu again
        print()


if __name__ == '__main__':
    main()
