import team

# 학생 등록
team.register_student(1,1,1, "I am one")
team.register_student(2,2,2, "Two")

# 학생 이름으로 조회
student = team.get_student_by_name("I am one")
print(student.grade)
print(student.class_num)
print(student.student_num)
print(student.name)

# 학생 전체 조회
for student in team.get_all_students():
    print(student.grade, student.class_num, student.student_num, student.name)

# 학생 수정
team.update_student(1, 1, 1, "one")
for student in team.get_all_students():
    print(student.grade, student.class_num, student.student_num, student.name)

# 학생 삭제
print(team.delete_student(1, 1, 1))


