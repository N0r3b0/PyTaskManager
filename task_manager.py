import json
from task import Task

class TaskManager:
    task_list: dict

    def __init__(self):
        pass



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
        
        
        
        # print(self.task_list["skills"][2])


    