from .file_handler import FileHandler
from .task import Task


class TaskManager:
    """
    This class is responsible for managing tasks. It provides methods to add, list, search, update and delete tasks.
    """

    def __init__(self):
        """
        Initializes the TaskManager instance. It calls the FileHandler.initialize_data() method to initialize the data
        and loads tasks from the JSON file using FileHandler.load_from_json() method.
        """

        FileHandler.initialize_data()

        self.tasks = FileHandler.load_from_json()

    def add_task(self, title, description=""):
        """
        Adds a task to the list of tasks. It creates a new Task instance, converts it to a dictionary, adds it to the
        list of tasks and saves the updated list.

        Args:
            title (str): The title of the task.
            description (str, optional): The description of the task. Defaults to "".

        Returns:
            Task: The newly created task.
        """
        # Create the task
        task = Task(title=title, description=description)

        # Convert the task to a dictionary
        task_dict = task.__dict__

        # Add the task to the list
        self.tasks.append(task_dict)

        # Save the updated list
        self._save()

        return task

    def list_tasks(self):
        """
        Lists all tasks.

        Returns:
            list: A list of all tasks.
        """
        return [task for task in self.tasks]

    def search_by_title(self, title):
        """
        Searches for tasks by title.

        Args:
            title (str): The title of the task.

        Returns:
            list: A list of tasks with the given title.
        """
        return [task for task in self.tasks if task["title"] == title]

    def search_by_description(self, description):
        """
        Searches for tasks by description.

        Args:
            description (str): The description of the task.

        Returns:
            list: A list of tasks with the given description.
        """
        return [task for task in self.tasks if task["description"] == description]

    def update_task_by_title(self, title, new_title=None, description=None):
        """
        Updates a task by title.

        Args:
            title (str): The title of the task to update.
            new_title (str, optional): The new title of the task. Defaults to None.
            description (str, optional): The new description of the task. Defaults to None.

        Returns:
            dict or None: The updated task if found, None otherwise.
        """
        for task in self.tasks:
            if task["title"] == title:
                if new_title:
                    task["title"] = new_title
                if description:
                    task["description"] = description
                self._save()
                return task
        return None

    def delete_task(self, title):
        """
        Deletes a task by title.

        Args:
            title (str): The title of the task to delete.
        """
        self.tasks = [task for task in self.tasks if task["title"] != title]
        self._save()

    def _save(self):
        """
        Saves the list of tasks to the JSON file using FileHandler.save_to_json() method.
        """
        FileHandler.save_to_json(self.tasks)
