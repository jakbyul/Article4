class Student:
    def __init__(self, grade, class_num, student_num, name):
        self.grade = grade
        self.class_num = class_num
        self.student_num = student_num
        self.name = name

# 학생 리스트
students = []

# 학생 등록
def register_student(grade, class_num, student_num, name):
    student = Student(grade, class_num, student_num, name)
    students.append(student)

# 학생 조회
def get_student(grade, class_num, student_num):
    for student in students:
        if student.grade == grade and student.class_num == class_num and student.student_num == student_num:
            return student
    return None

# 학생 이름으로 조회
def get_student_by_name(name):
    for student in students:
        if student.name == name:
            return student
    return None

# 학생 전체 조회
def get_all_students():
    return students

# 학생 수정
def update_student(grade, class_num, student_num, name):
    student = get_student(grade, class_num, student_num)
    if student:
        student.name = name
    else:
        print("학생을 찾을 수 없습니다.")

# 학생 삭제
def delete_student(grade, class_num, student_num):
    global students
    length = len(students)
    students = [student for student in students if student.grade != grade or student.class_num != class_num or student.student_num != student_num]
    return length != len(students)