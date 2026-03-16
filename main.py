import os
import task_manager
import sys

# python 
# main.py          0
# (function) add / delete / update / list      1
# (task title / number)      2
# (task title (update only)) 3 

# if CLI length is less than 2
# sys.exit(1)
if len(sys.argv) < 2:
    print("Provide a valid command: add , update, delete, list")
    sys.exit(1)
    
    
# valid commands: add, update, delete, list.
commands = ["add", "update", "delete", "list"]
# Else, exit.
if sys.argv[1] not in commands:
    sys.exit(1)
    
#-------------------------------------------------

#add
#must have length of >= 3. else, exit
#if command is add.
#Acquire the task title from the argument. 
#pass the title to the function in task_manager.py
#title = join all arguments after CLI[1] 
if sys.argv[1] == "add":
    if len(sys.argv) < 3:
        print("Task title required")
        sys.exit(1)
    title = " ".join(sys.argv[2:])

    task_manager.add_task(title)


#update
# must have length of 4.
# CLI[2] must be a number. else, exit
#if command is update. 
#pass the task id and title to the fuction on task_manager.py
if sys.argv[1] == "update":
    if len(sys.argv) < 4:
        print("Task ID & Task title required")
        sys.exit(1)
    if sys.argv[2].isdigit() == False:
        print("Enter a valid task ID to update")
        sys.exit(1)

    task_id = int(sys.argv[2])
    title = " ".join(sys.argv[3:])

    task_manager.update_task(task_id, title)


#delete
# must have length of 3.
# CLI[2] must be a number. else, exit
#if the command is delete.
#Acquire task ID from the command line and pass to task_manager.py

if sys.argv[1] == "delete":
    if len(sys.argv) < 3:
        print("Enter a task ID to delete")
        sys.exit(1)
    if sys.argv[2].isdigit() == False:
        print("Task ID must be a number")
        sys.exit(1)
        
    task_id = sys.argv[2]
    task_manager.delete_task(task_id)
        

#list
# if command is list
#pass command to task_manager.py list function.

if sys.argv[1] == "list":
    task_manager.list_all()
    