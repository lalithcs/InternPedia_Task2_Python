import os

# Function to load tasks from file
def load_tasks(file_name):
    tasks = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                task, status = line.strip().split(',')
                tasks.append({'task': task, 'status': status})
    return tasks

# Function to save tasks to file
def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['status']}\n")

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):
            status = "Done" if task['status'] == 'done' else "Undone"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("Your To-Do List is empty.")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({'task': task, 'status': 'undone'})
    print("Task added successfully!")

# Function to mark a task as done or undone
def toggle_task_status(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to toggle status: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['status'] = 'done' if tasks[index]['status'] == 'undone' else 'undone'
            print("Task status toggled successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the index of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function
def main():
    file_name = "todo.txt"
    tasks = load_tasks(file_name)

    while True:
        print("\nWelcome to the To-Do List Application!")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Toggle task status")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            toggle_task_status(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(file_name, tasks)
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
#thank you!!!!!