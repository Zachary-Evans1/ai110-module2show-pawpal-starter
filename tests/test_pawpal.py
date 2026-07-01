import pytest
from pawpal_system import Task, Pet


def test_mark_completed_changes_task_status():
    """Verify that calling mark_completed() actually changes a task's status."""
    task = Task(description="Feed the dog")
    assert task.completed is False

    task.mark_completed()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    """Verify that adding a task to a pet increases the pet's task count."""
    pet = Pet(name="Buddy", breed="Golden Retriever", owner_name="John")
    task = Task(description="Feed the dog")

    assert len(pet.get_tasks()) == 0

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1
