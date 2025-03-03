import os
from task_manager import display_tasks, add_task, remove_task, mark_task_completed, clear_completed_tasks
from task_storage import load_tasks, save_tasks

def clear_console():
    """Clear the console screen."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')

def wait_for_continue():
    """Wait for the user to press Enter to continue and then clear the console."""
    input("\n\nPress Enter to continue...")
    clear_console()

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Clear completed tasks")
        print("6. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                display_tasks(tasks)
                save_tasks(tasks)
                wait_for_continue()
            elif choice == 2:
                add_task(tasks)
                save_tasks(tasks)
                wait_for_continue()
            elif choice == 3:
                remove_task(tasks)
                save_tasks(tasks)
                wait_for_continue()
            elif choice == 4:
                mark_task_completed(tasks)
                save_tasks(tasks)
                wait_for_continue()
            elif choice == 5:
                clear_completed_tasks(tasks)
                save_tasks(tasks)
                wait_for_continue()
            elif choice == 6:
                print(f"Saving tasks: {tasks}")
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("\n\nInvalid choice. Please try again.")
                wait_for_continue()
        except ValueError:
            print("\n\nInvalid input. Please enter a number.")
            wait_for_continue()

if __name__ == "__main__":
    main()
