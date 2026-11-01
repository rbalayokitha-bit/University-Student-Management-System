from src.person import Person
from src.exceptions import InvalidMarksError


class Student(Person):

    def __init__(self, name, age, student_id, department, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.department = department
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise InvalidMarksError("Marks must be between 0 and 100.")

    def display_details(self):
        print("Student Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)
        print("Department:", self.department)
        print("Marks:", self.__marks)