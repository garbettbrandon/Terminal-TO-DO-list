import os

from colorama import Fore, init

init(autoreset=True)


def clear_screen():
    """
    Cleans the terminal screen.

    This function uses the 'os.system' function to execute the 'cls' command on Windows or the 'clear' command on Unix-based systems.
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_menu_header(title):
    """
    Displays a menu header with a title.

    Args:
        title (str): The title of the menu.

    This function clears the screen, prints a header with the title, and prints a footer with the same length as the title.
    """
    clear_screen()
    print(f"{Fore.CYAN}=" * (len(title) + 4))
    print(f"{Fore.CYAN}  {title}  ")
    print(f"{Fore.CYAN}=" * (len(title) + 4))


def show_main_menu():
    show_menu_header("TO-DO LIST MANAGER")
    """
    Displays the main menu of the TO-DO LIST MANAGER.

    This function shows a menu with the following options:
        - Add Task
        - List Tasks
        - Update Task
        - Search by Title
        - Search by Description
        - Delete Task
        - Quit

    Returns:
        str: The user's selection.
    """

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
    """
    Displays an error message.

    Args:
        message (str): The error message.

    This function prints an error message in red and waits for the user to press Enter to continue.
    """
    print(f"{Fore.RED}ERROR: {message}")
    input(f"{Fore.YELLOW}Press Enter to continue...")


def success_message(message):
    """
    Displays a success message.

    Args:
        message (str): The success message.

    This function prints a success message in green and waits for the user to press Enter to continue.
    """
    print(f"{Fore.GREEN}SUCCESS: {message}")
    input(f"{Fore.YELLOW}Press Enter to continue...")
