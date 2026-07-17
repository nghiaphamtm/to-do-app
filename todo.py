from storage import load_tasks, save_tasks
from utils import format_task


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, text):
        self.tasks.append({
            "text": text,
            "done": False
        })

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
        else:
            print("Invalid task number.")

    def display(self):
        if not self.tasks:
            print("No tasks.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(format_task(i, task))

    def load(self):
        self.tasks = load_tasks()

    def save(self):
        save_tasks(self.tasks)
