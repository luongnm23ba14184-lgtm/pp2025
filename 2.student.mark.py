import json
import os

# ============================
# CLASSES
# ============================

class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.id} {self.name} {self.dob}"


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.marks = {}

    def input_mark(self, course_id):
        self.marks[course_id] = input("Enter the student's mark for this course: ")

    def __str__(self):
        base_info = super().__str__()
        if self.marks:
            marks_info = " | Marks: " + " ".join([f"({cid} {mark})" for cid, mark in self.marks.items()])
            return base_info + marks_info
        return base_info

    def to_dict(self):
        return {"id": self.id, "name": self.name, "DoB": self.dob, "marks": self.marks}

    @staticmethod
    def from_dict(data):
        s = Student(data["id"], data["name"], data["DoB"])
        s.marks = data.get("marks", {})
        return s


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} {self.name}"

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @staticmethod
    def from_dict(data):
        return Course(data["id"], data["name"])


# ============================
# MANAGEMENT SYSTEM
# ============================

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.num_students = 0
        self.num_courses = 0
        self.load_data()

    # ----------------------------
    # JSON SAVE/LOAD
    # ----------------------------
    def save_data(self):
        with open("students.json", "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)
        with open("courses.json", "w") as f:
            json.dump([c.to_dict() for c in self.courses], f, indent=4)

    def load_data(self):
        if os.path.exists("students.json"):
            with open("students.json", "r") as f:
                self.students = [Student.from_dict(s) for s in json.load(f)]
        if os.path.exists("courses.json"):
            with open("courses.json", "r") as f:
                self.courses = [Course.from_dict(c) for c in json.load(f)]
        self.num_students = len(self.students)
        self.num_courses = len(self.courses)

    # ----------------------------
    # ORIGINAL FUNCTIONS (OOP STYLE)
    # ----------------------------
    def input_number(self, unit):
        return int(input(f"Enter the number of {unit} in this class: "))

    def input_infos(self, item_type, infos):
        item_data = {}
        for info in infos:
            item_data[info] = input(f"\tEnter the {item_type}'s {info}: ")
        return item_data

    def display(self, lst):
        for i, item in enumerate(lst):
            print(f"{i+1}. {item}")

    def list_students(self):
        if len(self.students) == 0:
            print("There aren't any students yet")
            return
        print("==> Here is the student list:")
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student}")

    def list_courses(self):
        if len(self.courses) == 0:
            print("There aren't any courses yet")
            return
        print("==> Here is the course list:")
        for i, course in enumerate(self.courses):
            print(f"{i+1}. {course}")

    def select(self, options, msg="Select: "):
        while True:
            try:
                s = int(input(msg))
                if s in options:
                    return s
            except:
                pass
            print("Invalid input. Try again.")

    def pause(self):
        input("Press Enter to continue...")

    # ----------------------------
    # MAIN MENU
    # ----------------------------
    def main(self):
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

            selection = self.select(range(0, 8))

            if selection == 0:
                print("Saving data...")
                self.save_data()
                print("Data saved. Bye!")
                break

            elif selection == 1:
                self.num_students = self.input_number("students")
                print(f"==> There are {self.num_students} student(s) in this class")

            elif selection == 2:
                if self.num_students == 0:
                    print("Please input the number of students first")
                    self.pause()
                    continue

                self.students = []
                for i in range(self.num_students):
                    print(f"Student No. {i+1}")
                    data = self.input_infos("student", ("id", "name", "DoB"))
                    self.students.append(Student(data["id"], data["name"], data["DoB"]))
                self.list_students()

            elif selection == 3:
                self.num_courses = self.input_number("courses")
                print(f"==> There are {self.num_courses} course(s) in this class")

            elif selection == 4:
                if self.num_courses == 0:
                    print("Please input the number of courses first")
                    self.pause()
                    continue

                self.courses = []
                for i in range(self.num_courses):
                    print(f"Course No. {i+1}")
                    data = self.input_infos("course", ("id", "name"))
                    self.courses.append(Course(data["id"], data["name"]))
                self.list_courses()

            elif selection == 5:
                self.list_courses()
                if len(self.courses) > 0:
                    selected_course = self.select(range(1, self.num_courses+1), "Select a course: ") - 1
                    course_id = self.courses[selected_course].id
                    for i in range(self.num_students):
                        print(f"Student No. {i+1} - {self.students[i].name}: ", end="")
                        self.students[i].input_mark(course_id)

            elif selection == 6:
                self.list_courses()

            elif selection == 7:
                self.list_students()

            self.pause()


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.main()
