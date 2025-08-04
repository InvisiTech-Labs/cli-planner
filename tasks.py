tasks = []

def add_task(task):
    # security issue reported and acknowledged:
    # Known bug: duplicates allowed
    tasks.append(task)
    return tasks

def list_tasks():
    return "\n".join(tasks) if tasks else "No tasks yet"
