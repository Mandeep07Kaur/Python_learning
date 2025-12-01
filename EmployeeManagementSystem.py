employees = [
    {"name" : "Manna", "age" : 21,"salary" : 5000000, "full_time" :True},
    {"name" : "Tanna", "age" : 45,"salary" : 7800000, "full_time" :True },
    {"name" : "Ruru", "age" : 75,"salary" : 456789, "full_time" : False}
]

def add_employees(employees, name, age, salary, full_time):
    new_employees = {"name": name, "age": age, "salary": salary, "full_time": full_time}
    employees.append(new_employees)
    return employees

def give_raise(employees, name, amount):
    for employee in employees:
        if employee["name"] == name:
            employee["salary"] += amount
            return employees
        
    print("Employee not found")
    return employees

def list_full_time(employees):
    full_time_list = []
    for employee in employees:
        if employee["full_time"] == True:
         full_time_list.append(employee["name"])
    return full_time_list
        
def list_part_time(employees):
    part_time_list = []
    for employee in employees:
        if employee["full_time"] == False:
            part_time_list.append(employee["name"])
    return part_time_list

        
def get_average_salary(employees):
    total_salary = 0
    
    for employee in employees:
        total_salary += employee["salary"]
    
    total_employees = len(employees)
    average = total_salary / total_employees
    
    return average

def search_employee(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee
    print("Employee not found")
    return None



print("---- INITIAL EMPLOYEES ----")
print(employees)

# 1. Add a new employee
employees = add_employees(employees, "Simran", 30, 600000, True)
print("\n---- AFTER ADDING EMPLOYEE ----")
print(employees)

# 2. Give a raise to Manna
employees = give_raise(employees, "Manna", 50000)
print("\n---- AFTER GIVING RAISE TO MANNA ----")
print(employees)

# 3. List full-time employees
print("\n---- FULL-TIME EMPLOYEES ----")
print(list_full_time(employees))

# 4. List part-time employees
print("\n---- PART-TIME EMPLOYEES ----")
print(list_part_time(employees))

# 5. Get average salary
print("\n---- AVERAGE SALARY ----")
print(get_average_salary(employees))

# 6. Search for an employee (existing)
print("\n---- SEARCH: Tanna ----")
print(search_employee(employees, "Tanna"))

# 7. Search for an employee (not existing)
print("\n---- SEARCH: Gopal ----")
print(search_employee(employees, "Gopal"))






    

