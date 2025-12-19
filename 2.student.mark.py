class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def __str__(self):
        info = f"{self.id} {self.name} {self.dob}"
        if self.marks:
            marks_str = " | Marks: " + " ".join([f"({cid} {m})" for cid, m in self.marks.items()])
            info += marks_str
        return info


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f"{self.id} {self.name}"


class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number(self, unit):
        return int(input(f"Enter the number of {unit} in this class: "))

    def input_student_infos(self, num_students):
        self.students = []
        for i in range(num_students):
            print(f"Student No. {i+1}")
            student_id = input("\tEnter student's id: ")
            name = input("\tEnter student's name: ")
            dob = input("\tEnter student's DoB: ")
            self.students.append(Student(student_id, name, dob))

    def input_course_infos(self, num_courses):
        self.courses = []
        for i in range(num_courses):
            print(f"Course No. {i+1}")
            course_id = input("\tEnter course id: ")
            name = input("\tEnter course name: ")
            self.courses.append(Course(course_id, name))

    def list_students(self):
        if not self.students:
            print("There aren't any students yet")
            return
        print("==> Here is the student list:")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses yet")
            return
        print("==> Here is the course list:")
        for i, course in enumerate(self.courses, 1):
            print(f"{i}. {course}")

    def input_marks(self):
        self.list_courses()
        if not self.courses:
            return
        selected_course = int(input("Select a course (number): ")) - 1
        course_id = self.courses[selected_course].id
        for i, student in enumerate(self.students, 1):
            mark = input(f"Student No. {i} - {student.name}: ")
            student.add_mark(course_id, mark)

    def run(self):
        num_students = 0
        num_courses = 0

        while True:
            print("====================================")
            print("Here are the functions of this application")
            print("0. Exit")
            print("1. Input number of students")
            print("2. Input students information (id, name, DoB)")
            print("3. Input number of courses")
            print("4. Input course information (id, name)")
            print("5. Input marks for student in a course")
            print("6. List courses")
            print("7. List students")
            print("====================================")

            try:
                selection = int(input("Select: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if selection == 0:
                print("Bye!")
                break
            elif selection == 1:
                num_students = self.input_number("students")
                print(f"==> There are {num_students} student(s) in this class")
            elif selection == 2:
                if num_students == 0:
                    print("Please input the number of students first")
                    input("Press Enter to continue...")
                    continue
                self.input_student_infos(num_students)
                self.list_students()
            elif selection == 3:
                num_courses = self.input_number("courses")
                print(f"==> There are {num_courses} course(s) in this class")
            elif selection == 4:
                if num_courses == 0:
                    print("Please input the number of courses first")
                    input("Press Enter to continue...")
                    continue
                self.input_course_infos(num_courses)
                self.list_courses()
            elif selection == 5:
                self.input_marks()
            elif selection == 6:
                self.list_courses()
            elif selection == 7:
                self.list_students()

            input("Press Enter to continue...")


if __name__ == "__main__":
    app = SchoolManagement()
    app.run()
