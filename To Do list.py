tasks = []
number = 1

while True:
    answer = input("> ")

    if answer.lower().strip() == "exit":
        print("Exiting the program...")
        break

    elif answer[0:3].lower() == "add":

        if answer.lower().strip() == "add":
            print("Incomplete Command... > add {Task you want to add}")

        elif answer[0:4].lower() == "add ":
            tasks.append(answer[4:].capitalize() + " - [Incomplete]")
        else:
            print("Invalid Command. Type 'help' to know more about commands.")

    elif answer.lower().strip() == "view":

        if tasks == []:
            print("There are no tasks to view.")

        else:
            for i in range(0,len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif answer.lower().strip() == "done":

        if tasks == []:
            print("There are no tasks to be completed")


        else:
            while True:
                print("Enter task number you want to mark as done ")

                try:
                    number = int(input("> "))

                except ValueError:
                    print("Enter a valid number")
                    continue

                if number < 1  or number > len(tasks):
                    print("Enter a valid number")
                    continue

                break

            if "[Incomplete]" in tasks[number-1]:
                tasks[number-1] = tasks[number-1].replace("[Incomplete]","[Complete]")
                print(f"{number}. {tasks[number-1]}")
            else:
                print(f"Task {number} is already completed")

    elif answer.lower().strip() == "delete":
        if tasks == []:
            print("There are no tasks to be deleted")

        else:
            while True:
                print("Enter task number you want to delete ")

                try:
                    number = int(input("> "))

                except ValueError:
                    print("Enter a valid number")
                    continue

                if number < 1 or number > len(tasks):
                    print("Enter a valid number")
                    continue
                break

            while True:
                print(tasks[number-1])
                print("Are you sure you want to delete above task? (Y)es/(N)o ")
                answer = input("> ")
                if answer.lower().strip() == "yes" or "y":
                    tasks.remove(tasks[number-1])
                    print(f"Task {number} Deleted.")
                elif answer.lower().strip() == "no" or "n":
                    print("Deletion request cancelled.")
                else:
                    print("Wrong input try again. ")
                    continue
                break


    elif answer.lower().strip() == "undo":

        if tasks == []:
            print("There are no tasks to mark as Incomplete")

        else:
            while True:
                print("Enter task number you want to mark as Incomplete ")

                try:
                    number = int(input("> "))

                except ValueError:
                    print("Enter a valid number")
                    continue

                if number < 1 or number > len(tasks):
                    print("Enter a valid number")
                    continue

                break
            if "[Complete]" in tasks[number-1]:
                tasks[number-1] = tasks[number-1].replace("[Complete]","[Incomplete]")
                print(f"{number}. {tasks[number - 1]}")
            else:
                print(f"Task {number} is already Incompleted")

    elif answer.lower().strip() == "help":
        print("""add {Task you want to add} - Add a new task
view - View all tasks you added
done - Mark tasks that are completed
undo - Mark completed tasks as incomplete again
delete - Delete tasks""")

    else:
        print("Invalid Command. Type 'help' to know more about commands.")
