import _sqlite3

conn = _sqlite3.connect('StudentDB')
c = conn.cursor()


exit_case = False

while exit_case == False:
    print("Enter 'help' for list of commands.")
    value = input("Enter a command: ")

    if value.lower() == "select":
        c.execute("SELECT * FROM Student")
        conn.commit()
        rows = c.fetchall()

        for row in rows:
            print(row)

    elif value.lower() == "add":
        correct = False
        while correct == False:
            f_name = input("Enter the student's first name: ")
            l_name = input("Enter the student's last name: ")
            gpa = input("Enter the student's GPA: ")
            major = input("Enter the student's Major: ")
            advisor = input("Enter the student's faculty advisor: ")

            gpa = float(gpa)

            print(
                "The Student is: " + f_name + " " + l_name + " GPA:" + str(gpa) + " Major: " + major + " Advisor: " + advisor)
            answer = input("Is this student correct: ")
            if (answer.lower() == 'yes' or answer.lower() == 'y'):
                correct = True
                sql = "INSERT INTO Student(FirstName, LastName, GPA, Major, FacultyAdvisor, isDeleted) VALUES (?,?,?,?,?,?)"
                values = (f_name, l_name, gpa, major, advisor, 0)
                c.execute(sql, values)
                conn.commit()

        print("Student was added successfully.")

    elif value.lower() == "update":
        correct = False
        f_name = ""
        l_name = ""
        while correct == False:
            f_name = input("Enter the first name of the student you wish to update: ")
            l_name = input("Enter the last name of the student you wish to update: ")

            print("Student: " + f_name + " " + l_name)
            answer = input("Is this the student you wish you update? ")

            if answer.lower() == 'yes' or answer.lower() == 'y':
                correct = True

        print("Do you wish to update the major, advisor, or both>")
        option = input("Enter your choice as outlined above (i.e. 'major' or 'advisor' or 'both': ")
        if option.lower() == "major":
            answer = False
            major = ""
            while answer == False:
                major = input("Enter the updated major: ")
                print("Student: " + f_name + " " + l_name + " Updated Major: " + major)
                answer = input("Is this correct?")
                if answer.lower() == 'yes' or answer.lower() == "y":
                    answer = True

            sql = "UPDATE Student SET Major = ? WHERE FirstName = ? AND LastName = ?"
            values = (major, f_name, l_name)
            c.execute(sql, values)
            conn.commit()

        elif option.lower() == "advisor":
            answer = False
            advisor = ""
            while answer == False:
                advisor = input("Enter the updated advisor: ")
                print("Student: " + f_name + " " + l_name + " Updated Advisor: " + advisor)
                answer = input("Is this correct?")
                if answer.lower() == 'yes' or answer.lower() == "y":
                    answer = True

            sql = "UPDATE Student SET FacultyAdvisor = ? WHERE FirstName = ? AND LastName = ?"
            values = (advisor, f_name, l_name)
            c.execute(sql, values)
            conn.commit()

        elif option.lower() == "both":
            answer = False
            major = ""
            advisor = ""
            while answer == False:
                major = input("Enter the updated major: ")
                advisor = input("Enter the updated advisor: ")
                print("Student: " + f_name + " " + l_name + " Updated Major: " + major + " Updated Advisor: " + advisor)
                answer = input("Is this correct?")
                if answer.lower() == 'yes' or answer.lower() == "y":
                    answer = True

            sql = "UPDATE Student SET Major = ?, FacultyAdvisor = ? WHERE FirstName = ? AND LastName = ?"
            values = (major, advisor, f_name, l_name)
            c.execute(sql, values)
            conn.commit()

        else:
            print("Invalid command.")

        print("Student was updated successfully.")


    elif value.lower() == 'delete':
        correct = False
        f_name = ""
        l_name = ""
        while correct == False:
            f_name = input("Enter the first name of the student you wish to remove: ")
            l_name = input("Enter the last name of the student you wish you remove: ")

            print("Student: " + f_name + " " + l_name)
            answer = input("Is this the right student you wish to remove?")
            if answer.lower() == "yes" or answer.lower() == "y":
                correct = True

        sql = "UPDATE Student SET isDeleted = ? WHERE FirstName = ? AND LastName = ?"
        values = (1, f_name, l_name)
        c.execute(sql, values)
        conn.commit()
        print("Student was updated successfully.")

    elif value.lower() == "display":
        display = input("Enter the category which you wish to view by ('gpa', 'major', or 'advisor'):")

        if display.lower() == "gpa":
            c.execute("SELECT * FROM Student GROUP BY GPA ORDER BY GPA DESC ")
            rows = c.fetchall()
            for row in rows:
                print(row)
        elif display.lower() == "major":
            c.execute("SELECT * FROM Student GROUP BY Major")
            rows = c.fetchall()
            for row in rows:
                print(row)
        elif display.lower() == "advisor":
            c.execute("SELECT * FROM Student GROUP BY FacultyAdvisor")
            rows = c.fetchall()
            for row in rows:
                print(row)
        else:
            print("Invalid Command.")

    elif value.lower() == 'help':
        print("select  : Displays all students and attributes"
              "add     : Prompts information to add new student to the table"
              "update  : Gives options to update a student's major, advisor, or both"
              "delete  : Soft deletes a student based off first and last name"
              "display : Displays student information grouped by GPA, major, or advisor"
              "help    : Returns commands"
              "exit    : Exits the program")

    elif value.lower() == "exit":
        exit_case = True

    else:
        continue

    print('\n')