# To-Do List Application in Python

# Function to display the menu
def display_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks in the to-do list
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("\n==== To-Do List ====")
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return
    try:
        task_index = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_index <= len(todo_list):
            todo_list[task_index - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the To-Do List application
def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()