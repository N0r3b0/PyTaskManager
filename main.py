import os, sys, argparse
from termcolor import colored
from task_manager import TaskManager

parser = argparse.ArgumentParser(description="Program for managing your tasks")

parser.add_argument("-l", "--list", type=str, help="name of the tasks list")
parser.add_argument("-c", "--create", type=str, help="create a new tasks list")
parser.add_argument("-a", "--add", nargs='+', help="use -l to choose list, add new tasks into the list")
parser.add_argument("-d", "--delete", nargs='+', help="use -l to choose list, delete tasks from the list")
parser.add_argument("-u", "--update", action="store_true", help="use -l to choose list, update task on the list")
parser.add_argument("-s", "--show", action="store_true", help="show all lists or 1 list if used with -l")
parser.add_argument("-v", "--version", action="store_true", help="program version and repository location")
args = parser.parse_args()

task = TaskManager()


if args.version:
    # 1.0.0: Init version

    print(f"{colored("PyTaskManager", "red")}: {colored("1.0.0", "magenta")}")
    print(f"{colored("Repo: ", "red")} https://{colored("github.com", "green")}/{colored("N0r3b0","cyan")}/{colored("PyTaskManager", "magenta")}")
    sys.exit(0)

if args.create:
    # create json file if doesnt exist
    task.create_task_list(args.create)
    pass

if args.list:
    # pull data from json
    task.open_task_list(args.list)
    pass

if args.list and args.add:  # Buy milk' 'Remember to get almond milk' 'false'
    # add task to the list 
    # [0] name [1] desc [2] done
    task.add_task(args.add)
    task.save_task_list(args.list)
    pass

if args.list and args.delete:
    # usun zadanie z listy
    pass

if args.list and args.update:
    # update zadania na liście
    pass


if args.list and args.show:
    pass
if args.show:
    pass