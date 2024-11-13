# Simple To-Do List Application in Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list"""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """Remove a task from the list"""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def show_tasks(self):
        """Display all tasks in the list"""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def menu(self):
        """Display the menu and process user input"""
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                task = input("Enter the task to add: ")
                self.add_task(task)
            elif choice == '2':
                task = input("Enter the task to remove: ")
                self.remove_task(task)
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("Exiting To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

# Main function to run the app
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()
