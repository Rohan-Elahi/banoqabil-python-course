# NAME = ROHAN ELAHI
#ROOL NUMBER = 40547
#EMAIL = relahi508@gmail.com

#importing date and time using library
import datetime

#creating txt file to save data of user input
#using list function to store data in list
Task_list = []  # Initialize an empty list to store tasks
file_path = "tasks.txt"  # Define the file path where tasks will be saved

# Function to load tasks from the file
def load_tasks_from_file():
    global Task_list  # Use the global Task_list variable
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                task_entry = line.strip().split(", ")  # Seperate function of each line by ", " to separate task and date
                Task_list.append({"Task": task_entry[0], "Date": task_entry[1]})  # Add task and date to Task_list as a dictionary
    except FileNotFoundError:
        Task_list = []  # If file not found, set Task_list to an empty list

# Function to save tasks to the file
def save_tasks_to_file():
    with open(file_path, "w") as file:
        for task_entry in Task_list:
            file.write(f"{task_entry['Task']}, {task_entry['Date']}\n")  # Write task and date to the file

# Function to insert a task into the to-do list
def insert_data():
    add_task = input("Enter Task: ")
    date_input = input("Enter the date (YYYY-MM-DD): ")

    user_datetime = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    dic = {
        "Task": add_task,
        "Date": user_datetime.strftime("%Y-%m-%d")
    }
    Task_list.append(dic)  # Add the task to Task_list
    print("TASK ADDED")

# Function to display all tasks in the to-do list
def show_alltask():
    for i, task_entry in enumerate(Task_list):
        print(f"Task {i + 1}: {task_entry['Task']}   Date: {task_entry['Date']}")

# Function to delete a task from the to-do list
def delete_task():
    show_alltask()
    task_to_delete = input("Enter the name of the task you want to delete: ")

    for task_entry in Task_list:
        if task_entry["Task"] == task_to_delete:
            Task_list.remove(task_entry)  # Remove the task from Task_list
            print(f"Task '{task_to_delete}' has been deleted.")
            break
    else:
        print(f"Task '{task_to_delete}' not found in the list.")
    print(Task_list)

# Function to update a task in the to-do list
def update_task():
    show_alltask()
    task_to_update = input("Enter the name of the task you want to update: ")

    for task_entry in Task_list:
        if task_entry["Task"] == task_to_update:
            new_task_name = input("Enter the new name for the task: ")
            new_date_input = input("Enter the new date for the task (YYYY-MM-DD): ")

            new_user_datetime = datetime.datetime.strptime(new_date_input, "%Y-%m-%d")

            task_entry["Task"] = new_task_name
            task_entry["Date"] = new_user_datetime.strftime("%Y-%m-%d")
            print(f"Task '{task_to_update}' has been updated.")
            break
    else:
        print(f"Task '{task_to_update}' not found in the list.")

# Function to display the menu
def menu():
    load_tasks_from_file()
    while True:
        print("---------------\t TO-DO-LIST MENU----------------")
        print("1 - Insert Task")
        print("2 - Display Task")
        print("3 - Delete Task")
        print("4 - Update Task")
        print("5 - Exit")
        choice = input("Enter the operation you want to perform: ")
        print()
        if choice == "1":
            insert_data()
        elif choice == "2":
            show_alltask()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Enter in update Task")
            update_task()
        elif choice == "5":
            save_tasks_to_file()
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

menu()  # Start the menu
