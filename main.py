from pawpal_system import Scheduler, Owner, Pet, Task

Owner = Owner()
Pet1 = Pet(name="Forrest", breed="Boxer", owner_name="Zach")
Pet2 = Pet(name="Hunter", breed="Golden Lab", owner_name="Zach")

Pet1.add_task(Task(description="Morning walk", duration=20, priority=3, time_of_day="9:00 AM"))
Pet1.add_task(Task(description="Feeding", duration=10, priority=2, time_of_day="12:00 PM"))
Pet1.add_task(Task(description="Fetch", duration=15, priority=1, time_of_day="2:00 PM"))

Pet2.add_task(Task(description="Morning walk", duration=25, priority=3, time_of_day="10:00 AM"))
Pet2.add_task(Task(description="Feeding", duration=12, priority=2, time_of_day="1:00 PM"))
Pet2.add_task(Task(description="Fetch", duration=15, priority=1, time_of_day="3:00 PM"))

Owner.add_pet(Pet1)
Owner.add_pet(Pet2)

Schedule = Scheduler()

Schedule.generate_daily_plan(Owner)

print("Today's Schedule:")
print(Schedule.daily_plan)