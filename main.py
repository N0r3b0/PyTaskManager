import os, sys, argparse
from termcolor import colored
from task_manager import TaskManager

parser = argparse.ArgumentParser(description="Program for managing your tasks")
subparsers = parser.add_subparsers(dest='command', help='Available commands')


parser.add_argument("-l", "--list", type=str, help="name of the tasks list")
parser.add_argument("-c", "--create", type=str, help="create a new tasks list")
parser.add_argument("-a", "--add", nargs='+', help="adds new task. Use -l to choose the list and than -a with 3 possible arguments (name required): name description status. Status options: true, yes, 1, done")
parser.add_argument("-d", "--delete", type=str, help="deletes the task. Use -l to choose the list and than -a with an id of the task you want to remove")

# parser for update
update_parser = subparsers.add_parser('update', aliases=['u'], help='Use -l to choose list and use u to update the task. Use u -h to see parameters')
update_parser.add_argument('--id', type=int, required=True, help='Task ID - required')
update_parser.add_argument('--name', help='Task name')
update_parser.add_argument('--desc', help='Task description')
update_parser.add_argument('--status', help='Task status')

parser.add_argument("-s", "--show", action="store_true", help="show available task lists or print tasks from the list if used with -l")
parser.add_argument("-v", "--version", action="store_true", help="program version and repository location")

parser.add_argument("--clear", action="store_true", help="clear all task lists, if used with -l clears only selected task list")

args = parser.parse_args()

task = TaskManager()
task.open_tasklists()


if args.version:
    # 1.0.0: Init version

    print(f"{colored("PyTaskManager", "red")}: {colored("1.0.0", "magenta")}")
    print(f"{colored("Repo: ", "red")} https://{colored("github.com", "green")}/{colored("N0r3b0","cyan")}/{colored("PyTaskManager", "magenta")}")
    sys.exit(0)

if args.clear and not args.list:
    task.clear_tasklists()

if args.create:
    # create json file if doesnt exist
    task.create_task_list(args.create)
    task.open_tasklists()
    pass

if args.list:
    # pull data from json
    task.open_task_list(args.list)
    pass

if args.clear and args.list:
    task.clear_task_list(args.list)

if args.list and args.add:  # Buy milk' 'Remember to get almond milk' 'false'
    # add task to the list 
    # [0] name [1] desc [2] done
    task.add_task(args.add)
    task.save_task_list(args.list)
    pass

if args.list and args.delete:
    # remove task from the list
    task.remove_task(args.delete)
    task.save_task_list(args.list)
    

if args.list and args.show:
    task.show_tasks()
if not args.list and args.show:
    task.show_tasklists()


# TASK UPDATE
if args.command in ('update', 'u') and not args.list:
    parser.error("Update command require to pass the list name using (-l/--list)")

if args.command in ('update', 'u') and args.list and args.id:
    print(f"Updating the task with an ID: {args.id} and parameters:")
    details = {'id': args.id}
    if args.name:
        print(f" - New name: {args.name}")
        details["name"] = args.name
    if args.desc:
        print(f" - New description: {args.desc}")
        details["description"] = args.desc
    if args.status:
        print(f" - New status: {args.status}")
        details["status"] = args.status

    
    task.update_task(details)
    task.save_task_list(args.list)
    pass