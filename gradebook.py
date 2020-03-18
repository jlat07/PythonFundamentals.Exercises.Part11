from typing import List, Dict
from enum import Enum
import uuid


class AliveStatus(Enum):
    deceased = 0
    alive = 1


class Person(self):
    def __init__(self, first_name: str, last_name: str, dob: str):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = AliveStatus.alive
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def update_first_name(self, first_name: str):
        self.first_name = first_name
    
    def update_last_name(self, last_name: str):
        self.last_name = last_name
    
    def update_dob(self, dob: str):
        self.dob = dob
    
    def update_status(self, alive: AliveStatus):
        self.status = alive


class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Person.__init__(self, first_name, last_name, dob)
        self.instructor_id = f"Instructor_{uuid.uuid4()}"


class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Person.__init__(self, first_name, last_name, dob)
        self.student_id = f"Student_{uuid.uuid4()}"


class ZipCodeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Person.__init__(self, first_name, last_name, dob)


class CollegeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: str, ):
        Person.__init__(self, first_name, last_name, dob)


class Classroom:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.instructors: Dict[str, Instructor] = {}
    
    def add_instructor(self, instructor: Instructor):
        if instructor.instructor_id not in self.instructors:
            self.instructors[Instructor.instructor_id] = instructor
    
    def remove_instructor(self, instructor: Instructor):
        if instructor.instructor_id in self.instructors:
            del self.instructors[Instructor.instructor_id]
    
    def add_student(self, student: Student):
        if student.student_id not in self.students:
            self.students[Student.student_id] = student
    
    def remove_student(self, student: Student):
        if student.student_id in self.students:
            del self.students[Student.student_id]
    
    def print_instructors(self):
        for key, value in self.instructors.items():
            print(f"{key}: {value}")
    
    def print_students(self):
        for key, value in self.students.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    pass

'''
python3 -m unittest test_gradebook.py
'''
