class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_completed(self, task_index):
        self.tasks[task_index] = self.tasks[task_index] + " (Completed)"

    def display_list(self):
        print("To-Do List:")
        for task in self.tasks:
            print(task)

# Example usage
todo = ToDo()
todo.add_task("Finish Python Assignment")
todo.add_task("Buy Sticky Notes")
todo.mark_completed(0)
todo.display_list()


