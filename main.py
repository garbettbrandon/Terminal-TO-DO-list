import os

from colorama import Fore, Style, init

init()

tasks = []


def limpiar_terminal():
    # Limpieza de terminal multiplataforma
    os.system("cls" if os.name == "nt" else "clear")


def add_task():
    title = input("Enter the title of the task: ")
    content = input("Enter the content of the task: ")
    tasks.append({"title": title, "content": content})
    print("Task added successfully!")


def delete_task():
    title = input("Enter the title of the task to delete: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")


def update_task():
    title = input("Enter the title of the task to update: ")
    for task in tasks:
        if task["title"] == title:
            new_title = input("Enter the new title of the task: ")
            new_content = input("Enter the new content of the task: ")
            task["title"] = new_title
            task["content"] = new_content
            print("Task updated successfully!")
            return
    print("Task not found.")


def display_tasks():
    for task in tasks:
        print("--------------------")
        print("Title:", task["title"])
        print("Content:", task["content"])
        print("--------------------")


def search_by_title():
    title = input("Enter the title of the task to search for: ")
    for task in tasks:
        if task["title"] == title:
            print("Title:", task["title"])
            print("Content:", task["content"])
            print("--------------------")
            return
    print("Task not found.")


def search_by_content():
    content = input("Enter the content of the task to search for: ")
    for task in tasks:
        if task["content"] == content:
            print("Title:", task["title"])
            print("Content:", task["content"])
            print("--------------------")
            return
    print("Task not found.")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print_error("Please enter a number.")
            continue

        choice = int(choice)

        if 0 <= choice <= 6:
            if choice == 1:
                add_task()
            elif choice == 2:
                display_tasks()
            elif choice == 3:
                search_by_title()
            elif choice == 4:
                search_by_content()
            elif choice == 5:
                update_task()
            elif choice == 6:
                delete_task()
            elif choice == 0:
                print_goodbye_message()
                break
        else:
            print_error("Invalid choice. Please try again.")


def print_menu():
    print(
        "\n"
        + Fore.CYAN
        + "--------------------Menu-----------------------"
        + Style.RESET_ALL
    )
    print("1. Add new task")
    print("2. Display all tasks")
    print("3. Search for a task by title")
    print("4. Search for a task by content")
    print("5. Update a task")
    print("6. Delete a task")
    print("0. Exit")
    print("------------------------------------------------\n")


def print_error(message):
    print(f"\nError: {message}")


def print_goodbye_message():
    print("\nThank you for using the To-Do List App. Goodbye!")


if __name__ == "__main__":
    limpiar_terminal()
    main()
