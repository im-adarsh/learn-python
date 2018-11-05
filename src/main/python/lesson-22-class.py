from src.main.python.classes.Student import Student

student_1 = Student("Mike", "Business", 3.1, False)
student_2 = Student("Pam", "Art", 3.2, True)

print(student_1.name)
print(student_2.name)


print(student_1.on_honor_rol())
