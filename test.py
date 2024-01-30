import team
import unittest


# # 학생 등록
# team.register_student(1,1,1, "I am one")
# team.register_student(2,2,2, "Two")
# team.register_student(1,1,1, "I am a")

# # 학생 이름으로 조회
# student = team.get_student_by_name("I am one")
# print(student.grade)
# print(student.class_num)
# print(student.student_num)
# print(student.name)

# # 학생 전체 조회
# for student in team.get_all_students():
#     print(student.grade, student.class_num, student.student_num, student.name)

# # 학생 수정
# team.update_student(1, 1, 1, "one")
# for student in team.get_all_students():
#     print(student.grade, student.class_num, student.student_num, student.name)

# # 학생 삭제
# print(team.delete_student(1, 1, 1))
# for student in team.get_all_students():
#     print(student.grade, student.class_num, student.student_num, student.name)



class LeapYearTest(unittest.TestCase):
    def test_leap_year(self):
    
        # 학생 등록
        self.assertTrue(team.register_student(1,1,1, "I am one"))
        self.assertFalse(team.register_student(1,1,1, "I am a"))

        # 학생 이름으로 조회
        student = team.get_student_by_name("I am one")
        self.assertEqual(student.grade,1)
        self.assertEqual(student.class_num,1)
        self.assertEqual(student.student_num,1)
        self.assertEqual(student.name,"I am one")

        # 학생 수정
        team.update_student(1, 1, 1, "one")
        self.assertEqual(team.get_student(1,1,1).name,"one")

        # 학생 삭제
        self.assertTrue(team.delete_student(1, 1, 1))
        self.assertFalse(team.get_student(1,1,1))



if __name__ == '__main__':
    unittest.main()

