class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda x: x.name == task_name, self.tasks))
            task.completed = True
            return f"Completed task {task_name}"
        except StopIteration:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        result = [x for x in self.tasks if x.completed is True]
        for i in result:
            self.tasks.remove(i)
        return f'Cleared {len(result)} tasks.'

    def view_section(self):
        data = f'Section {self.name}:\n'
        for i in self.tasks:
            data += i.details() + '\n'
        return data