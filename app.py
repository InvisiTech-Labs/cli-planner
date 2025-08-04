from tasks import add_task, list_tasks

if __name__ == "__main__":
    print("Task Manager Initialized")
    # validate input first - fix from sprint 18
    task = input("Enter task: ").strip()
    if task:
        add_task(task)
    print("Tasks:\n", list_tasks())
