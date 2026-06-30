from dataclasses import dataclass


@dataclass
class Task:
    """Represents a pet care task."""
    taskName: str
    priority: int
    completed: bool
    duration: int

    def mark_completed(self) -> None:
        pass

    def update_priority(self, priority: int) -> None:
        pass

    def update_duration(self, duration: int) -> None:
        pass

    def getTaskName(self) -> str:
        pass

    def setTaskName(self, name: str) -> None:
        pass

    def getPriority(self) -> int:
        pass

    def setPriority(self, priority: int) -> None:
        pass

    def isCompleted(self) -> bool:
        pass

    def getDuration(self) -> int:
        pass

    def setDuration(self, duration: int) -> None:
        pass


@dataclass
class Pet:
    """Represents a pet with associated tasks."""
    petName: str
    petBreed: str
    ownerName: str
    taskList: list[Task]

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: int) -> None:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def getPetName(self) -> str:
        pass

    def setPetName(self, name: str) -> None:
        pass

    def getPetBreed(self) -> str:
        pass

    def setPetBreed(self, breed: str) -> None:
        pass

    def getOwnerName(self) -> str:
        pass

    def setOwnerName(self, name: str) -> None:
        pass


@dataclass
class Planner:
    """Generates and explains daily pet care plans."""
    constraints: str
    explanation: str
    dailyPlan: str

    def generate_daily_plan(self, pet: Pet) -> None:
        pass

    def explain_plan(self) -> None:
        pass

    def getConstraints(self) -> str:
        pass

    def setConstraints(self, constraints: str) -> None:
        pass

    def getExplanation(self) -> str:
        pass

    def getDailyPlan(self) -> str:
        pass


@dataclass
class PawPal:
    """Main application that manages pets and generates care plans."""
    pets: list[Pet]
    planner: Planner

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet_id: int) -> None:
        pass

    def get_pet(self, pet_id: int) -> Pet:
        pass

    def run_planner(self, pet: Pet) -> None:
        pass

    def getPets(self) -> list[Pet]:
        pass
