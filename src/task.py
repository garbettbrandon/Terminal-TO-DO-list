from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: int = field(default_factory=int)
    title: str = ""
    description: str = ""
    status: str = "Pendiente"
    created_at: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    completed_at: str = ""
