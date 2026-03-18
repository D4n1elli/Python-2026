# --To do list--

# add a task to the list
def task_add(tasks_list):
    new_item = input("\nNew task: ")
    tasks_list.append(new_item)
    print("Task added.\n")

# remove a task from the list
def task_remove(tasks_list):
    print("\nPlease select which task you want removed:")
    # print list
    i = 1
    for item in tasks_list:
        print(f"Task {i}: {item}")
        i += 1

    # get task to be removed and validates input
    while True:
        removed = int(input("Number of task to remove: "))
        if removed > len(tasks_list) or removed <= 0:
            print("Try a valid number")
            continue
        break

    tasks_list.remove(tasks_list[removed-1])

# display tasks in terminal
def task_view(tasks_list):
    if tasks_list:
        i = 1
        for item in tasks_list:
            print(f"Task {i}: {item}")
            i += 1
    else:
        print("No tasks yet!")
    print("\n")

# main
def main():
    print("\n--To do list--")

    tasks_list = []

    while True:
        # print menu
        print("1 - add task\n2 - remove task\n3 - view list")
        print("0 - quit\n")

        # option input
        action = int(input("Select an option from the menu: "))
        if action < 0 or action > 3:
            print("Try a valid option.")
            continue   

        # calls functions with the option selected
        if action == 0:
            break
        if action == 1:
            task_add(tasks_list)
        if action == 2:
            task_remove(tasks_list)
        if action == 3:
            task_view(tasks_list)

# call main function
main()