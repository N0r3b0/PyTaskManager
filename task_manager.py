import json
import os
from task import Task

class TaskManager:
    task_list: dict = {}
    task_lists: dict = {}

    def generate_id(self, dict: dict):
        if not dict:
            return "1"
        return str(max(int(key) for key in dict.keys()) + 1)

    # TASKLISTS
    def save_tasklists(self, file: str):
        id = self.generate_id(self.task_lists)
        self.task_lists.update({id: {'task_list_name': file}})
        with open("data/task_lists.json", 'w') as f:
                json.dump(self.task_lists, f, indent=2)
    
    def open_tasklists(self):
        try:
            if os.path.getsize("data/task_lists.json") != 0:
                with open("data/task_lists.json", 'r') as f:
                    self.task_lists = json.load(f)
        except FileNotFoundError:
            file = open("data/task_lists.json", 'w')
            file.close()
    
    def clear_tasklists(self):
        for id, name in self.task_lists.items():
            if os.path.exists(f"data/{name['task_list_name']}.json"):
                os.remove(f"data/{name['task_list_name']}.json")
                print(f"data/{name['task_list_name']}.json has been removed")
        with open("data/task_lists.json", 'w') as f:
                print("All task lists have been cleared")
        


    # TASKLIST
    def create_task_list(self, file: str):
        try:
            with open(f"data/{file}.json", 'x') as f:  # 'x' creates file, raises FileExistsError if it exists
                print(f"Task list {file} created") 
                self.save_tasklists(file)
        except FileExistsError:
            print(f"The list {file} already exists")

   
    def open_task_list(self, file: str):
        try:
            with open(f"data/{file}.json", 'r') as f:
                content = f.read().strip()
                self.task_list = json.loads(content) if content else {}

        except FileNotFoundError:
            print(f"The list {file} does not exist")
            self.task_list = []


    def save_task_list(self, file: str):
        with open(f"data/{file}.json", 'w') as f:
            json.dump(self.task_list, f, indent=2)

    def clear_task_list(self, file: str):
        with open(f"data/{file}.json", 'w') as f:
                print("List has been cleared")
            

    def show_tasklists(self):
        print("📋 Task Lists:")
        print("-" * 40)
        for id, name in self.task_lists.items():
            print(f"{id}. {name['task_list_name']}")

    # TASK MANAGMENT

    def show_tasks(self):
        print("📋 Task List:")
        print("-" * 40)
        for task_id, task in self.task_list.items():
            status_icon = "✅" if task["status"] == "done" else "❌"
            print(f"ID: {task_id}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']} {status_icon}")
            print("-" * 40)

    
    def add_task(self, details):
        # details -> name, desc, status
        task = Task(details)
        task_id = self.generate_id(self.task_list)
        self.task_list[task_id] = task.to_dict()
        print(f"Task added with ID {task_id}")


    def remove_task(self, id: str):
        try:
            self.task_list.pop(id)
            print(f"Removed task with ID: {id} ")
        except:
            print("Wrong task id")
    

    def update_task(self, details: dict):
        # details -> --id --name, --desc, --status
        task_id = str(details["id"])
        if details.get("name"):
            self.task_list[task_id]["name"] = details["name"]
        if details.get("description"):
            self.task_list[task_id]["description"] = details["description"]
        if details.get("status"):
            self.task_list[task_id]["status"] = details["status"]
    