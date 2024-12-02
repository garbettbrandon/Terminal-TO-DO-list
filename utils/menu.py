import os

from colorama import Fore, init

init(autoreset=True)


def clear_screen():
    """Cleans the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu_header(title):
    clear_screen()
    print(f"{Fore.CYAN}=" * (len(title) + 4))
    print(f"{Fore.CYAN}  {title}  ")
    print(f"{Fore.CYAN}=" * (len(title) + 4))


def show_main_menu():
    show_menu_header("TO-DO LIST MANAGER")
    menu_options = [
        "Add Task",
        "List Tasks",
        "Update Task",
        "Search by Title",
        "Search by Description",
        "Delete Task",
        "Quit",
    ]

    for index, option in enumerate(menu_options, 1):
        print(f"{Fore.GREEN}{index}. {option}")

    return input(f"{Fore.YELLOW}Select an option: ")


def error_message(message):
    """Shows an error message"""
    print(f"{Fore.RED}ERROR: {message}")
    input(f"{Fore.YELLOW}Press Enter to continue...")


def success_message(message):
    """Shows a success message"""
    print(f"{Fore.GREEN}SUCCESS: {message}")
    input(f"{Fore.YELLOW}Press Enter to continue...")
