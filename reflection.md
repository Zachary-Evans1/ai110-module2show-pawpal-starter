# PawPal+ Project Reflection

## 1. System Design

The three core actions I came up with are the following:
1. Add a pet, and add any tasks you want to track with that pet.
2. View a pets daily plan, and be able to read the explanation given with that plan.
3. Set owner constraints and preferences

**a. Initial design**

- Briefly describe your initial UML design.

My initial UML design was focused on breaking the system into four main classes, Pet, Task, Planner, and PawPal. Each class was designed to represent a clear part of the pet care app and keep responsibilities seperate.

- What classes did you include, and what responsibilities did you assign to each?

I originally designed four classes,  Pet, Task, Planner, and PawPal,

The Pet classes responsibilities is to store information about a pet, such as its name, breed/type, owner and a list of tasks for the pet. It also manages adding, removing and retrieving tasks for a specific task.

The Task classes responsibilities is to represent individual pet care activites, like feeding or walking the animal. It stores details like the task name, priority, duration, and the tasks completion status. It also inludes methods for updating these values.

The Planner class was responsible for generating a daily care plan based on a pet's tasks and any constraints. It also stores the generated schedule and an explanation of why a specific daily plan was generated.

The PawPal class acted as the main system manager. It stored a list of all pets and connected everything together by allowing pets to be added or removed and by running the planner to generate daily schedules.

**b. Design changes**

- Did your design change during implementation?

Yes, it did.

- If yes, describe at least one change and why you made it.

One major change I made was removing the getters and setters and making the code overall more pythonic. I made this change because it made each class have unnecessary functions, that I only put in because I am more used to Java/C++.

Another change was renaming and restructuring two of my classes to better match the assignment. Planner was changed into Scheduler, and PawPal was changed into Owner to better reflect their responsibilities in the system.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
