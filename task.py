from enum import Enum
class Status(Enum):
    IN_PROGRESS = 0
    DONE = 1
    UNFINISHED = -1

class Task:
    name: str = ""
    description: str = ""
    status: Status
    
    def __str__(self):
        return f"name: {self.name} \
        \ndescription: {self.description} \
        \nstatus: {self.status.name.lower()}"
    
    def __init__(self, name = "basic task", description = "basic description", status = Status.UNFINISHED):
        self.name = name
        self.description = description
        self.status = status





