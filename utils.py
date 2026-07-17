def format_task(number, task):
    status = "✓" if task["done"] else " "
    return f"{number}. [{status}] {task['text']}"
