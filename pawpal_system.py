from dataclasses import dataclass, field


@dataclass
class Constraint:
    """Represents a constraint for pet care tasks (e.g., time range, allergies, duration limits)."""
    constraint_type: str
    value: str


@dataclass
class Task:
    """Represents a pet care task."""
    id: int
    name: str
    priority: int
    completed: bool = False
    duration: int = 0
    time_of_day: str | None = None

    def mark_completed(self) -> None:
        pass

    def update_priority(self, priority: int) -> None:
        pass

    def update_duration(self, duration: int) -> None:
        pass


@dataclass
class Pet:
    """Represents a pet with associated tasks."""
    id: int
    name: str
    breed: str
    owner_name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: int) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass


@dataclass
class Planner:
    """Generates and explains daily pet care plans."""
    constraints: str
    current_pet: Pet | None = None
    plan_date: str | None = None
    constraint_list: list[Constraint] = field(default_factory=list)
    explanation: str = ""
    daily_plan: str = ""

    def generate_daily_plan(self, pet: Pet) -> None:
        pass

    def explain_plan(self) -> None:
        pass


@dataclass
class PawPal:
    """Main application that manages pets and generates care plans."""
    pets: list[Pet] = field(default_factory=list)
    planner: Planner | None = None

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: int) -> None:
        pass

    def get_pet(self, pet_id: int) -> Pet:
        pass

    def run_planner(self, pet: Pet) -> None:
        pass
