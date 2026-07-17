from todo import TodoList

def menu():
    print("\n=== TO-DO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Save")
    print("5. Exit")

def main():
    todo = TodoList()
    todo.load()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            todo.display()

        elif choice == "2":
            task = input("Task: ")
            todo.add(task)

        elif choice == "3":
            index = int(input("Task number: ")) - 1
            todo.complete(index)

        elif choice == "4":
            todo.save()
            print("Tasks saved.")

        elif choice == "5":
            todo.save()
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
