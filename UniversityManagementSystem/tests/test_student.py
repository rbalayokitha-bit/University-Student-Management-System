import pytest

from src.student import Student
from src.person import Person
from src.exceptions import InvalidMarksError


# Test 1: Student creation
def test_student_creation():

    student = Student("Bala", 18, "101", "AI&DS", 85)

    assert student.name == "Bala"
    assert student.age == 18
    assert student.student_id == "101"
    assert student.department == "AI&DS"


# Test 2: Get marks
def test_get_marks():

    student = Student("Bala", 18, "101", "AI&DS", 85)

    assert student.get_marks() == 85


# Test 3: Update marks
def test_set_marks():

    student = Student("Bala", 18, "101", "AI&DS", 85)

    student.set_marks(95)

    assert student.get_marks() == 95


# Test 4: Invalid marks
def test_invalid_marks():

    student = Student("Bala", 18, "101", "AI&DS", 85)

    with pytest.raises(InvalidMarksError):
        student.set_marks(150)


# Test 5: Person display
def test_person_display(capsys):

    person = Person("Bala", 18)

    person.display_details()

    output = capsys.readouterr().out

    assert "Bala" in output
    assert "18" in output


# Test 6: Student display
def test_student_display(capsys):

    student = Student("Bala", 18, "101", "AI&DS", 85)

    student.display_details()

    output = capsys.readouterr().out

    assert "Bala" in output
    assert "AI&DS" in output
    assert "85" in output