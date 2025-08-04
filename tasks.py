tasks = []

def add_task(task):
    tasks.append(task)
    return tasks

def list_tasks():
    return "\n".join(tasks) if tasks else "No tasks yet"
