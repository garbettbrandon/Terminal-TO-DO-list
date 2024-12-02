from dataclasses import dataclass, field


@dataclass
class Task:
    id: int = field(default_factory=int)
    title: str = ""
    description: str = ""
