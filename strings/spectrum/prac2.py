todo_list = []  # A list to store the tasks in the to-do list

while True:  # Infinite loop to keep the To-Do List application running until the user chooses to quit
    print("\n===== To-Do List Application =====")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")  # User input for choosing the operation

    if choice == '1':
        print("\n===== To-Do List =====")
        if not todo_list:
            print("No tasks in the list.")
        else:
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            print("=====================")
    elif choice == '2':
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"\n'{task}' has been added to the To-Do list.")
    elif choice == '3':
        if todo_list:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed_task = todo_list.pop(index - 1)
                print(f"\n'{removed_task}' has been removed from the To-Do list.")
            else:
                print("\nInvalid task index.")
        else:
            print("\nNo tasks to remove.")
    elif choice == '4':
        break  # Exit the loop and end the program if the user chooses to quit
    else:
        print("Invalid choice. Please try again.")
