from src.student import Student
from src.storage import StudentStorage


student1 = Student("Bala", 18, "101", "AI&DS", 85)

student2 = Student("Ravi", 19, "102", "CSE", 90)

students = [student1, student2]


storage = StudentStorage()


# JSON operations
storage.save_students(students, "data/students.json")

storage.load_students("data/students.json")


# CSV operations
storage.save_csv(students, "data/students.csv")

storage.load_csv("data/students.csv")