from json_db_lite import JSONDatabase
from datetime import datetime

# инициализация объекта
small_db = JSONDatabase(file_path='students.json')


# получаем все записи
def json_to_dict_list():
    return small_db.get_all_records()


# добавляем студента
def add_student(student: dict):
    # Проверяем, является ли 'date_of_birth' строкой
    if isinstance(student['date_of_birth'], str):
        # Преобразуем строку в объект datetime
        student['date_of_birth'] = datetime.strptime(student['date_of_birth'], '%Y-%m-%d')
    # Форматируем дату в строку
    student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
    small_db.add_records(student)
    return True


# обновляем данные по студенту
def upd_student(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


# удаляем студента
def dell_student(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True