from .file_handler import FileHandler
from .task import Task


class TaskManager:
    def __init__(self):
        
        FileHandler.initialize_data()

        self.tasks = FileHandler.load_from_json()

    def add_task(self, title, description=""):
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
        return [task for task in self.tasks]

    def search_by_title(self, title):
        return [task for task in self.tasks if task["title"] == title]

    def search_by_description(self, description):
        return [task for task in self.tasks if task["description"] == description]

    def update_task_by_title(self, title, new_title=None, description=None):
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
        self.tasks = [task for task in self.tasks if task["title"] != title]
        self._save()

    def _save(self):
        FileHandler.save_to_json(self.tasks)
