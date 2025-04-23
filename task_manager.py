import json
from task import Task

class TaskManager:
    task_list: dict = {}


    def create_task_list(self, file: str):
        try:
            with open(f"{file}.json", 'x') as f:  # 'x' creates file, raises FileExistsError if it exists
                json.dump([], f)  
        except FileExistsError:
            print(f"The list {file} already exists")

   
    def open_task_list(self, file: str):
        try:
            with open(f"{file}.json", 'r') as f:
                self.task_list = json.load(f)
        except:
            print(f"The list {file} does not exist")


    def save_task_list(self, file: str):
        with open(f"{file}.json", 'w') as f:
            json.dump(self.task_list, f, indent=2)
            
    
    # TASK MANAGMENT

    def generate_task_id(self):
        if not self.task_list:
            return "1"
        return str(max(int(key) for key in self.task_list.keys()) + 1)

    
    def add_task(self, details):
        # details -> name, desc, status
        task = Task(details)
        task_id = self.generate_task_id()
        self.task_list[task_id] = task.to_dict()
        print(f"Task added with ID {task_id}")

    