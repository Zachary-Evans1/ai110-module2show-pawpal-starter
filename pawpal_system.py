from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents a single pet care activity (task)."""
    description: str
    frequency: str = "once"
    time_of_day: str | None = None
    completed: bool = False
    priority: int = 0
    duration: int = 0

    def mark_completed(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def update_priority(self, priority: int) -> None:
        """Update the priority level of this task."""
        self.priority = priority

    def update_duration(self, duration: int) -> None:
        """Update the estimated duration of this task."""
        self.duration = duration


@dataclass
class Pet:
    """Represents a pet with associated tasks."""
    name: str
    breed: str
    owner_name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task_index: int) -> None:
        """Remove a task from this pet's task list by index."""
        self.tasks.pop(task_index)

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    pets: list[Pet] = field(default_factory=list)
    scheduler: "Scheduler | None" = None

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet_index: int) -> None:
        """Remove a pet from the owner's pet list by index."""
        self.pets.pop(pet_index)

    def get_pet(self, pet_id: int) -> Pet:
        """Return a pet by index."""
        return self.pets[pet_id]

    def run_scheduler(self) -> None:
        """Generate a daily plan if a scheduler is assigned."""
        if self.scheduler:
            self.scheduler.generate_daily_plan(self)

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Scheduler:
    """The 'brain' that retrieves, organizes, and manages tasks across pets."""
    plan_date: str | None = None
    constraints: list[str] = field(default_factory=list)
    explanation: str = ""
    daily_plan: str = ""

    def generate_daily_plan(self, owner: Owner) -> None:
        """Generate and store a daily task plan for all pets."""
        if not owner.pets:
            self.daily_plan = "No pets to schedule."
            self.explanation = "Owner has no pets."
            return

        plan_lines = [f"Daily Plan for {self.plan_date or 'Today'}\n"]

        for pet in owner.pets:
            plan_lines.append(f"Pet: {pet.name}")

            sorted_tasks = sorted(pet.get_tasks(), key=lambda t: t.time_of_day or "")

            if not sorted_tasks:
                plan_lines.append("  No tasks scheduled.")
            else:
                for task in sorted_tasks:
                    time_str = task.time_of_day or "No time set"
                    plan_lines.append(f"  {time_str} - {task.description} (Priority: {task.priority})")

            plan_lines.append("")

        self.daily_plan = "\n".join(plan_lines)
        self.explanation = "Schedule organized by pet with tasks sorted chronologically."

    def explain_plan(self) -> str:
        """Return the explanation of the generated daily plan."""
        return self.explanation