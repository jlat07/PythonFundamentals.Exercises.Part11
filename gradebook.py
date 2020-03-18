class AliveStatus:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width


This class must inherit from Enum.
It must have two possible symbolic names:
* Deceased - associated with the value 0
* Alive - associated with the value 1


class Person(Enum):
    def __init__(self, first_name: int, last_name: int, dob: str, ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = 0
* alive (of type AliveStatus)

    def update_first_name():
    
    def update_last_name():
    
    def update_dob():
    
    def update_status():


class Instructor(Person):
    def __init__(self, first_name: int, last_name: int, dob: str, ):
        Person.__init__(self, first_name, last_name, dob)
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = 0
        self.instructor_id = "Instructor_"()

class Student(Person):
    def __init__(self, first_name: int, last_name: int, dob: str, ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = 0
        self.student_id = "Student_"()


class ZipCodeStudent(Student):
    def __init__(self, first_name: int, last_name: int, dob: str, ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = 0
        self.student_id = "Student_"()


class CollegeStudent(Student):
    def __init__(self, first_name: int, last_name: int, dob: str, ):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.status = 0
        self.student_id = "Student_"()


class Classroom(self):
    def __init__ (self, students: Student, instructors: Instructor):
        self.students = students
        self.instructors = instructors
        
    def add_instructor():
    
    def remove_instructor():
    
    def add_student():
    
    def remove_student():
    
    def print_instructors():
    
    def print_students():



```
 python3 -m unittest test_gradebook.py