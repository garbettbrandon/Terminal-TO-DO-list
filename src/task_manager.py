from datetime import datetime

from .file_handler import FileHandler
from .task import Task


class TaskManager:
    def __init__(self):
        # Inicializamos datos al crear la instancia
        FileHandler.initialize_data()

        # Cargamos las tareas
        self.tasks = FileHandler.load_from_json()

        # Establecemos el próximo ID
        self.next_id = max([int(task.get('id', 0)) for task in self.tasks],
                           default=0) + 1

    def add_task(self, title, description=""):
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task.__dict__)
        self.next_id += 1
        self._save()
        return task

    def list_tasks(self, status=None):
        if status:
            return [task for task in self.tasks if task["status"] == status]
        return self.tasks

    def update_task(self, task_id, title=None, description=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                self._save()
                return task
        return None

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completada"
                task["completed_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")
                self._save()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self._save()

    def _save(self):
        FileHandler.save_to_json(self.tasks)
