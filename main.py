import os, sys, argparse
from termcolor import colored

parser = argparse.ArgumentParser(description="Program for managing your tasks")

parser.add_argument("-l", "--list", action="store_true", help="name of the tasks list")
parser.add_argument("-a", "--add", nargs='+', help="use -l to choose list, add new tasks into the list")
parser.add_argument("-d", "--delete", nargs='+', help="use -l to choose list, delete tasks from the list")
parser.add_argument("-u", "--update", action="store_true", help="use -l to choose list, update task on the list")
parser.add_argument("-s", "--show", action="store_true", help="show all lists or 1 list if used with -l")
parser.add_argument("-v", "--version", action="store_true", help="program version and repository location")
args = parser.parse_args()

if args.version:
    # 1.0.0: Init version

    print(f"{colored("PyTaskManager", "red")}: {colored("1.0.0", "magenta")}")
    print(f"{colored("Repo: ", "red")} https://{colored("github.com", "green")}/{colored("N0r3b0","cyan")}/{colored("PyTaskManager", "magenta")}")
    sys.exit(0)


if args.list and args.add:
    # dodaj zadania lub zadanie do listy
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