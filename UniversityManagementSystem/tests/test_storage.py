import json
import csv

from src.student import Student
from src.storage import StudentStorage


def test_save_json(tmp_path):

    student = Student("Bala", 18, "101", "AI&DS", 85)

    storage = StudentStorage()

    filename = tmp_path / "students.json"

    storage.save_students([student], filename)

    with open(filename, "r") as file:
        data = json.load(file)

    assert data[0]["name"] == "Bala"
    assert data[0]["marks"] == 85


def test_save_csv(tmp_path):

    student = Student("Bala", 18, "101", "AI&DS", 85)

    storage = StudentStorage()

    filename = tmp_path / "students.csv"

    storage.save_csv([student], filename)

    with open(filename, "r") as file:
        data = list(csv.DictReader(file))

    assert data[0]["Name"] == "Bala"
    assert data[0]["Department"] == "AI&DS"
    assert data[0]["Marks"] == "85"