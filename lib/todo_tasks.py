class todo_tasks():
    def __init__(self):
        self._tasks = []

    def add_task(self, text):
        self._tasks.append(text)

    def show_tasks(self):
        return self._tasks
    
    def remove_task(self, text):
        self._tasks.remove(text)
