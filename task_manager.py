def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            status = 'Done' if task['completed'] else 'Pending'
            print(f"{idx}. {task['task']} - {status}")
            if 'due_date' in task:
                print(f"   Due Date: {task['due_date']}")
            if 'priority' in task:
                print(f"   Priority: {task['priority']}")

def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (low, medium, high): ")

    task = {
        'task': task_name,
        'completed': False,
    }

    if due_date:
        task['due_date'] = due_date
    if priority:
        task['priority'] = priority

    tasks.append(task)
    print(f"Task '{task_name}' added!")

def remove_task(tasks):
    """Remove a task by index."""
    display_tasks(tasks)
    try:
        task_index = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(f"Task '{tasks[task_index]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def clear_completed_tasks(tasks):
    """Remove all completed tasks."""
    tasks[:] = [task for task in tasks if not task['completed']]
    print("Completed tasks cleared!")
