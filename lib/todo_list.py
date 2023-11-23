class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        list2 = []
        for item in self.todo_list:
            if item.complete == False:
                list2.append(item)
        return list2

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        list2 = []
        for item in self.todo_list:
            if item.complete == True:
                list2.append(item)
        return list2

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for item in self.todo_list:
            item.complete = True
        