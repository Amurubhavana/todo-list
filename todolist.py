class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
