from .file_handler import FileHandler
from .task import Task


class TaskManager:
    def __init__(self):
        # Inicializamos datos al crear la instancia
        FileHandler.initialize_data()

        # Cargamos las tareas
        self.tasks = FileHandler.load_from_json()

        # Establecemos el próximo ID
        # Usamos max con un valor predeterminado de 0 y convertimos a entero
        self.next_id = (
            max([int(task.get("id", 0)) for task in self.tasks], default=0) + 1
        )

    def add_task(self, title, description=""):
        # Creamos la tarea con el ID actual
        task = Task(id=self.next_id, title=title, description=description)

        # Convertimos la tarea a diccionario para guardar
        task_dict = task.__dict__

        # Añadimos la tarea a la lista
        self.tasks.append(task_dict)

        # Incrementamos el ID para la próxima tarea
        self.next_id += 1

        # Guardamos los cambios
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

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self._save()

    def _save(self):
        FileHandler.save_to_json(self.tasks)
