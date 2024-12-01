from colorama import init, Fore
import os

init(autoreset=True)


def clear_screen():
    """Limpia la pantalla de la terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu_header(title):
    """Muestra un encabezado para los menús"""
    clear_screen()
    print(Fore.CYAN + "=" * (len(title) + 4))
    print(Fore.CYAN + f"  {title}  ")
    print(Fore.CYAN + "=" * (len(title) + 4))


def show_main_menu():
    """Muestra el menú principal"""
    show_menu_header("TO-DO LIST MANAGER")
    menu_options = [
        "Añadir Tarea",
        "Listar Tareas",
        "Actualizar Tarea",
        "Completar Tarea",
        "Eliminar Tarea",
        "Salir",
    ]

    for index, option in enumerate(menu_options, 1):
        print(Fore.GREEN + f"{index}. {option}")

    return input(Fore.YELLOW + "Seleccione una opción: ")


def show_list_submenu():
    """Submenú para listar tareas"""
    show_menu_header("LISTAR TAREAS")
    print(Fore.GREEN + "1. Todas las Tareas")
    print(Fore.GREEN + "2. Tareas Pendientes")
    print(Fore.GREEN + "3. Tareas Completadas")
    print(Fore.RED + "0. Volver al Menú Principal")
    return input(Fore.YELLOW + "Seleccione una opción: ")


def error_message(message):
    """Muestra un mensaje de error"""
    print(Fore.RED + f"ERROR: {message}")
    input(Fore.YELLOW + "Presione Enter para continuar...")


def success_message(message):
    """Muestra un mensaje de éxito"""
    print(Fore.GREEN + f"ÉXITO: {message}")
    input(Fore.YELLOW + "Presione Enter para continuar...")
