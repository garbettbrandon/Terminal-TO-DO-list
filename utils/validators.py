def validate_task_title(title):
    """
    Validates that the title is not empty and has between 3 and 50 characters.
    """
    if not title:
        raise ValueError("The title cannot be empty")
    if len(title) < 3:
        raise ValueError("The title must have at least 3 characters")
    if len(title) > 50:
        raise ValueError("The title cannot have more than 50 characters")

    return title


def validate_task_title_exists(title, available_tasks):
    if title not in [task["title"] for task in available_tasks]:
        raise ValueError(f"No task found with the title {title}")

    return title
