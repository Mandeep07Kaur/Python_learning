students = [
    {"name": "Mandeep", "grade": 95, "passed": True},
    {"name": "Manna", "grade": 55, "passed": False},
    {"name": "Deepu", "grade": 85, "passed": True}
]

def add_student(students, name, grade):
    new_student = {"name" : name, "grade" : grade, "passed" : grade>=50}
    students.append(new_student)
    return students

def update_grade(students, name, new_grade):
    for student in students:
        if student["name"] == name:
           student["grade"] = new_grade
           student["passed"] = new_grade >= 50
        return students

def get_average(students):
    total = 0
    for student in students:
        total += student["grade"]

    count = len(students) 
    average = total / count
    return average

def list_failed(students):
    failed = []     
    for student in students:      
        if student["passed"] == False:
            failed.append(student["name"])
    return failed   

def search(students, name):
    for student in students:
        if student["name"] == name:
           return student
        
    print("Student not found")
    return None
