import sys

from colorama import Fore

from src.task_manager import TaskManager
from utils.menu import error_message, show_main_menu, success_message
from utils.validators import validate_task_title, validate_task_title_exists


def add_task(task_manager):
    title = input(f"{Fore.GREEN}Enter the task title: ")
    try:
        validated_title = validate_task_title(title)
        description = input(f"{Fore.GREEN}Enter task description: ")
        task_manager.add_task(validated_title, description)
        success_message("Task added successfully")
    except ValueError as e:
        error_message(str(e))


def list_tasks(task_manager):
    tasks = task_manager.list_tasks()

    if not tasks:
        error_message("No tasks found")
    else:
        # display tasks
        for task in tasks:
            print(f"{Fore.CYAN}Title:", task["title"])
            print(f"{Fore.CYAN}Description:", task["description"])
            print("\n")

        input(f"{Fore.YELLOW}Press Enter to continue...")


def update_task(task_manager):
    title = input(f"{Fore.GREEN}Enter the title of the task to update: ")
    try:
        validate_task_title_exists(title, task_manager.tasks)
        new_title = input(f"{Fore.GREEN}Enter the NEW title of the task: ")
        validate_task_title(new_title)
        description = input(
            f"{Fore.GREEN}Enter the NEW description of the task (optional): "
        )
        task_manager.update_task_by_title(title, new_title, description)
        success_message("Task updated successfully")
    except ValueError as e:
        error_message(str(e))


def delete_task(task_manager):
    title = input(f"{Fore.GREEN}Enter the title of the task to delete: ")
    try:
        validated_title = validate_task_title_exists(title, task_manager.tasks)
        task_manager.delete_task(validated_title)
        success_message("Task deleted successfully")
    except ValueError as e:
        error_message(str(e))


def search_by_title(task_manager):
    title = input(f"{Fore.GREEN}Enter the title of the task to search: ")
    try:
        tasks = task_manager.search_by_title(title)
        if not tasks:
            error_message("No tasks found with that title")
        else:
            for task in tasks:
                print(f"{Fore.CYAN}Title:", task["title"])
                print(f"{Fore.CYAN}Description:", task["description"])
                print("\n")
        input(f"{Fore.YELLOW}Press Enter to continue...")
    except ValueError as e:
        error_message(str(e))


def search_by_description(task_manager):
    description = input(f"{Fore.GREEN}Enter the description of the task to search: ")
    try:
        tasks = task_manager.search_by_description(description)
        if not tasks:
            error_message("No tasks found with that description")
        else:
            for task in tasks:
                print(f"{Fore.CYAN}Title:", task["title"])
                print(f"{Fore.CYAN}Description:", task["description"])
                print("\n")
        input(f"{Fore.YELLOW}Press Enter to continue...")
    except ValueError as e:
        error_message(str(e))


def handle_error(e):
    error_message(str(e))
    sys.exit(1)


def main():

    task_manager = TaskManager()

    while True:
        try:
            option = show_main_menu()

            if option == "1":  # Añadir tarea
                add_task(task_manager)
            elif option == "2":  # Listar tareas
                list_tasks(task_manager)
            elif option == "3":  # Actualizar tarea
                update_task(task_manager)
            elif option == "4":  # Buscar tarea por titulo
                search_by_title(task_manager)
            elif option == "5":  # Buscar tarea por descripcion
                search_by_description(task_manager)
            elif option == "6":  # Eliminar tarea
                delete_task(task_manager)
            elif option == "7":  # Salir
                # Antes de salir, guardamos en JSON
                task_manager._save()
                break
        except Exception as e:
            handle_error(e)


if __name__ == "__main__":
    main()
