def add_mark(marks, new_mark):
    marks.append(new_mark)
    return marks

marks = [85, 92]
marks = add_mark(marks, 78)
marks = add_mark(marks, 88)

def get_average(marks):
    average = sum(marks) / len(marks)
    return average

print(marks)
print (get_average(marks))