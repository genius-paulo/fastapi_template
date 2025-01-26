import pytest
from json_db_lite import JSONDatabase
from utils import json_to_dict_list, add_student, upd_student, dell_student

# инициализация объекта
small_db = JSONDatabase(file_path='students.json')


def test_json_to_dict_list():
    students = json_to_dict_list()
    assert students is not None
    assert isinstance(students, list)


def test_add_student():
    student = {'name': 'John', 'age': 30, 'date_of_birth': '1990-01-01'}
    check = add_student(student)
    assert check is True


def test_upd_student():
    upd_filter = {'name': 'John'}
    new_data = {'age': 31}
    check = upd_student(upd_filter, new_data)
    assert check is True


def test_dell_student():
    key = 'name'
    value = 'John'
    check = dell_student(key, value)
    assert check is True

