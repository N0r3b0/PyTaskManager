import json
from enum import Enum

class Status(Enum):
    DONE = 1
    NOT_DONE = 0
    def to_str(self):
        return self.name.lower()

class Task:
    id: int = 0
    name: str = ""
    description: str = ""
    status: Status = Status.NOT_DONE
    
    def __init__(self, details):
        self.name = details[0]
        if len(details) > 1:
            self.description = details[1]
        if len(details) > 2:
            done_str = details[2].lower()
            if done_str in ("true", "yes", "1", "done"):
                self.status = Status.DONE


    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status.to_str()
        }

    





