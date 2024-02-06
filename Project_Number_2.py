import datetime

Task_list = []
file_path = "tasks.txt"

def load_tasks_from_file():
    global Task_list
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                task_entry = line.strip().split(", ")
                Task_list.append({"Task": task_entry[0], "Date": task_entry[1]})
    except FileNotFoundError:
        Task_list = []

def save_tasks_to_file():
    with open(file_path, "w") as file:
        for task_entry in Task_list:
            file.write(f"{task_entry['Task']}, {task_entry['Date']}\n")


def insert_data():
    add_task = input("Enter Task: ")
    date_input = input("Enter the date (YYYY-MM-DD): ")

    user_datetime = datetime.datetime.strptime(date_input , "%Y-%m-%d")
    dic = {
            "Task": add_task,
            "Date": user_datetime.strftime("%Y-%m-%d")
        }
    
    Task_list.append(dic)
    print("TASK ADDED")


def show_alltask():
    for i, task_entry in enumerate(Task_list):
        print(f"Task {i + 1}: {task_entry['Task']}   Date: {task_entry['Date']}")
 



def delete_task():
    show_alltask()  
    task_to_delete = input("Enter the name of the task you want to delete: ")

    for task_entry in Task_list:
        if task_entry["Task"] == task_to_delete:
            Task_list.remove(task_entry)
            print(f"Task '{task_to_delete}' has been deleted.")
            break
                    
    else:
        print(f"Task '{task_to_delete}' not found in the list.")

    print(Task_list)



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

menu()
