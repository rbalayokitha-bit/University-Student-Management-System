import json
import csv


class StudentStorage:

    # Save student details into JSON
    def save_students(self, students, filename):

        data = []

        for student in students:

            student_data = {
                "name": student.name,
                "age": student.age,
                "student_id": student.student_id,
                "department": student.department,
                "marks": student.get_marks()
            }

            data.append(student_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Student data saved successfully in JSON!")

    # Read student details from JSON
    def load_students(self, filename):

        with open(filename, "r") as file:
            data = json.load(file)

        print("Student data loaded successfully from JSON!")

        for student in data:
            print(student)

    # Save student details into CSV
    def save_csv(self, students, filename):

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Name",
                "Age",
                "Student ID",
                "Department",
                "Marks"
            ])

            for student in students:

                writer.writerow([
                    student.name,
                    student.age,
                    student.student_id,
                    student.department,
                    student.get_marks()
                ])

        print("Student data saved successfully in CSV!")

    # Read student details from CSV
    def load_csv(self, filename):

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            print("\nCSV Student Details:")

            for student in reader:
                print(student)