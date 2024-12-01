import sys

from colorama import Fore

from src.task_manager import TaskManager
from src.file_handler import FileHandler
from utils.menu import (
    show_main_menu,
    show_list_submenu, error_message,
    success_message
)
from utils.validators import validate_task_id, validate_task_title


def add_task(task_manager):
    title = input(Fore.GREEN + "Ingrese el título de la tarea: ")
    try:
        validated_title = validate_task_title(title)
        description = input(Fore.GREEN + "Ingrese la descripción (opcional): ")
        task_manager.add_task(validated_title, description)
        success_message("Tarea añadida con éxito")
    except ValueError as e:
        error_message(str(e))


def list_tasks(task_manager):
    submenu_option = show_list_submenu()
    if submenu_option == "1":
        tasks = task_manager.list_tasks()
    elif submenu_option == "2":
        tasks = task_manager.list_tasks(status="Pendiente")
    elif submenu_option == "3":
        tasks = task_manager.list_tasks(status="Completada")
    else:
        return

    if not tasks:
        error_message("No hay tareas para mostrar")
    else:
        # display tasks
        for task in tasks:
            print(Fore.CYAN + "ID:", task["id"])
            print(Fore.CYAN + "Título:", task["title"])
            print(Fore.CYAN + "Descripción:", task["description"])
            print(Fore.CYAN + "Estado:", task["status"])
            print(Fore.CYAN + "Fecha de Completado:", task["completed_at"])
            print(Fore.CYAN + "Fecha de Creación:", task["created_at"])
            print("\n")

        input(Fore.YELLOW + "Presione Enter para continuar...")


def update_task(task_manager):
    task_id = input(Fore.GREEN + "Ingrese el ID de la tarea a actualizar: ")
    try:
        validated_id = validate_task_id(task_id, task_manager.tasks)
        title = input(
            Fore.GREEN + "Ingrese el título de la tarea (opcional): ")
        description = input(
            Fore.GREEN + "Ingrese la descripción de la tarea (opcional): "
        )
        task_manager.update_task(validated_id, title, description)
        success_message("Tarea actualizada con éxito")
    except ValueError as e:
        error_message(str(e))


def delete_task(task_manager):
    task_id = input(Fore.GREEN + "Ingrese el ID de la tarea a eliminar: ")
    try:
        validated_id = validate_task_id(task_id, task_manager.tasks)
        task_manager.delete_task(validated_id)
        success_message("Tarea eliminada con éxito")
    except ValueError as e:
        error_message(str(e))


def complete_task(task_manager):
    task_id = input(Fore.GREEN + "Ingrese el ID de la tarea a completar: ")
    try:
        validated_id = validate_task_id(task_id, task_manager.tasks)
        task_manager.complete_task(validated_id)
        success_message("Tarea completada con éxito")
    except ValueError as e:
        error_message(str(e))


def convert_data(task_manager):
    task_manager._save()
    success_message("Datos convertidos con éxito")
    input(Fore.YELLOW + "Presione Enter para continuar...")


def handle_error(e):
    error_message(str(e))
    sys.exit(1)


def main():

    # Al iniciar, convertimos CSV a JSON si existe
    try:
        FileHandler.convert_csv_to_json()
    except Exception as e:
        print(Fore.YELLOW + f"Aviso: No se pudo convertir CSV a JSON - {e}")

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
            elif option == "4":  # Completar tarea
                complete_task(task_manager)
            elif option == "5":  # Eliminar tarea
                delete_task(task_manager)
            elif option == "6":  # Salir
                # Antes de salir, guardamos en CSV
                try:
                    FileHandler.save_to_csv(task_manager.tasks)
                    print(Fore.GREEN + "Datos guardados en CSV correctamente.")
                except Exception as e:
                    error_message(f"Error al guardar datos: {e}")
                break
        except Exception as e:
            handle_error(e)


if __name__ == "__main__":
    main()
