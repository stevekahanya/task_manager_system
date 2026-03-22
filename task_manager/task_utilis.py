from task_manager import validation

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    try:
        # These will raise ValueError if they fail
        validation.validate_task_title(title)
        validation.validate_task_description(description)
        validation.validate_due_date(due_date)
        
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
    except ValueError as e:
        print(f"Validation Error: {e}")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid index")

def view_pending_tasks(tasks=tasks):
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['title']}")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / len(tasks)) * 100.0
    return progress
