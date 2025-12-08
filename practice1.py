students = []
courses = []
marks = []

def validStudentFormat(line):
    return len(line.split("|")) == 3

def validCourseFormat(line):
    return len(line.split("|")) == 2

def validMarkFormat(line):
    return len(line.split("|")) == 2


def inputStudent():
    line = input("Input (id|name|DoB): ")

    while not validStudentFormat(line):
        print("This is wrong ,agin input: id|name|dob")
        line = input("Input Student (id|name|DoB): ")
        
    return line.split("|")
    
def inputCourse():
    line = input("Input Course (id|name): ")
    
    while not validCourseFormat(line):
        print("This wrong: id|name")
        line = input("Input Course (id|name): ")
        
    return line.split("|")

def inputMark():
    line = input(" Input Mark(student_id|mark): ")
    
    while not validMarkFormat(line):
        print("This wrong: student_id|mark")
        line = input("Input Mark(student_id|mark): ")
        
    return line.split("|")

def inputValidMark():
    student_id, mark = inputMark()
    
    while not any(student_id == student["id"] for student in students):
        print("The id is not exit")
        student_id, mark = inputMark()
        
    return student_id, mark


def inputStudentList():
    n = int(input("Input the number of student: "))
    
    for i in range(n):
        print(f"\n--- Student{i+1} ---")
        id, name, DoB = inputStudent()
        students.append({
            "id" : id,
            "name" : name,
            "DoB" : DoB
        })
        
def inputCourseList():
    n = int(input("\n The number of Course: "))
    
    for i in range(n):
        print(f"\n Course {i+1} ---")
        id, name = inputCourse()
        courses.append({
            "id" : id,
            "name" : name,
        })    
    
def inputMarkList():
    print("\nMark list is unvalue:")
    for course in courses:
        print(f'{course["id"]} - {course["name"]}')
        
    course_id = input("\nChọn id môn học để nhập điểm: ")
    
    while not any(course_id == course["id"] for course in courses):
        course_id = input("Chọn id môn học hợp lệ: ")
       
    n = int(input("Input the Mark: "))
    
    for i in range(n):
        print(f"\n--- Điểm {i+1} ---")
        student_id, mark = inputValidMark()
        marks.append({
            "course_id" : course_id,
            "student_id" : student_id,
            "mark" : mark
        })
        
def listingStudent():
    print("\nDanh sách sinh viên:")
    print(students)
    
def listingCourse():
    print("\nDanh sách môn học:")
    print(courses)
    
def listingMark():
    print("\nDanh sách điểm:")
    print(marks)
    
# --- Chương trình ---
inputStudentList()
inputCourseList()
inputMarkList()

listingCourse()
listingMark()
listingStudent()
