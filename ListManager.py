def add_task(todo_list, task):
    todo_list.append(task)
    return todo_list

def mark_done(task):
    return task + " completed"

todo_list = []

todo_list = add_task(todo_list, "Study Python")
todo_list = add_task(todo_list, "Go gym")
todo_list = add_task(todo_list, "Clean room")

print(todo_list)

done_task = mark_done(todo_list[0])
print(done_task)
