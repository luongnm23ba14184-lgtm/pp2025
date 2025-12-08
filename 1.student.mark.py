# Input a number
def input_number(unit):
    return int(input(f"Enter the number of {unit} in this class: "))

# Ask the user to enter info for an item
def input_infos(item_type, infos):
    item = {}
    for info in infos:
        item[info] = input(f"\tEnter the {item_type}'s {info}: ")
    return item

# Display list of items
def display(lst):
    for i, item in enumerate(lst):
        print(f"{i+1}. {item}")

# Input the student mark in a course
def input_mark(student, course_id):
    if "marks" not in student:
        student["marks"] = {}
    student["marks"][course_id] = input("Enter the student's mark for this course: ")

# List students
def list_students(students):
    if len(students) == 0:
        print("There aren't any students yet")
        return
    
    print("==> Here is the student list:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student['id']} {student['name']} {student['DoB']}", end="")

        if "marks" in student:
            print("\nMarks (CourseId Mark): ", end="")
            for course_id, mark in student["marks"].items():
                print(f"({course_id} {mark})", end="\t")
        print()

# List courses
def list_courses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
        return

    print("==> Here is the course list:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['id']} {course['name']}")

# Select an option safely
def select(options, msg="Select: "):
    while True:
        try:
            s = int(input(msg))
            if s in options:
                return s
        except:
            pass
        print("Invalid input. Try again.")

# Fake pause to match teacher style
def pause():
    input("Press Enter to continue...")
def main():
    students = []
    courses = []
    num_students = 0
    num_courses = 0

    while True:
     selection = select(range(0, 8))
     if selection == 0:
            break
     elif selection == 1:
          num_students = input_number("students")
          print(f"==> There are {num_students} student(s) in this class")

     elif selection == 2:
            if num_students == 0:
                print("Please input the number of students first")
                pause()
                continue

            students = []
            for i in range(num_students):
                print(f"Student No. {i+1}")
                students.append(input_infos("student", ("id", "name", "DoB")))
            
            list_students(students)

     elif selection == 3:
            num_courses = input_number("courses")
            print(f"==> There are {num_courses} course(s) in this class")

     elif selection == 4:
            if num_courses == 0:
                print("Please input the number of courses first")
                pause()
                continue

            courses = []
            for i in range(num_courses):
                print(f"Course No. {i+1}")
                courses.append(input_infos("course", ("id", "name")))

            list_courses(courses)

     elif selection == 5:
            list_courses(courses)
            if len(courses) > 0:
                selected_course = select(range(1, num_courses+1), "Select a course: ") - 1
                course_id = courses[selected_course]["id"]

                for i in range(num_students):
                    print(f"Student No. {i+1} - {students[i]['name']}: ", end="")
                    input_mark(students[i], course_id)

     elif selection == 6:
            list_courses(courses)

     elif selection == 7:
            list_students(students)

     else:
            print("Invalid input. Please try again.")
     pause()


if __name__ == "__main__":
    main()
