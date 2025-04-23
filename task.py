from enum import Enum
class Status(Enum):
    DONE = 1
    NOT_DONE = 0

class Task:
    name: str = ""
    description: str = ""
    status: Status
    
    def __init__(self, details):
        self.name = details[0]
        self.description = details[1] if len(details) > 1 else ""
        done_str = details[2].lower() if len(details) > 2 else "false"
        if done_str in ("true", "yes", "1", "done"):
            self.status = Status.DONE.name.lower()

    





