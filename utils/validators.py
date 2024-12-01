def validate_task_title(title):
    """
    Valida que el título de la tarea tenga entre 3 y 50 caracteres
    """
    if not title:
        raise ValueError("El título no puede estar vacío")
    if len(title) < 3:
        raise ValueError("El título debe tener al menos 3 caracteres")
    if len(title) > 50:
        raise ValueError("El título no puede exceder 50 caracteres")
    return title


def validate_task_id(task_id, available_tasks):
    """
    Valida que el ID de tarea exista
    """
    try:
        task_id = int(task_id)
    except ValueError:
        raise ValueError("El ID debe ser un número entero")

    if task_id not in [task["id"] for task in available_tasks]:
        raise ValueError(f"No existe una tarea con el ID {task_id}")

    return task_id
