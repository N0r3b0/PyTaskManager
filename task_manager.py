import json
from task import Task

class TaskManager:
    task_list: dict


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

    
    # TASK MANAGMENT
    def add_task(self, details):
        # details -> name, desc, status
        task = Task(details)
        # print(task.name, task.description, task.status)
        
        
        
        # print(self.task_list["skills"][2])


    