employees = [{"name": "Mandeep", "present": True},
             {"name": "Aman", "present": False},
             {"name": "Priya", "present": True}
             
]

def count_present(employees):
    count = 0
    for emp in employees:
        if emp["present"] == True:
            count += 1
    return count

print("Prsent:", count_present(employees))

    