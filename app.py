from tasks import add_task, list_tasks

if __name__ == "__main__":
    print("Task Manager Initialized")
    task = input("Enter task: ")
    add_task(task)
    print("Tasks:", list_tasks())
