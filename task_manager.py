import os
import json
from datetime import datetime

#load
#check for the file.
#if the file does not exist, create a new file
#with an empty list as its content.
filename = "tasks.json"

def load_file():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = json.load(file)
#if it does exists
#open the file and load the data into a list.
    else:
        tasks = []
        with open(filename, "w") as file:
         json.dump([], file)
        
    return tasks     

#save
#write to the file. 
def save_file(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


#-----------------------------------------


#add
#load the list with load_file 
#Acquire the components of the task
#ID - check for the highest existing ID (max ID) then n+1 it.
#If no ID is found, use ID 1 for the task.
#Title will be passed from main.py. 
#Creates at: current date
#Updated at: null
#append the task to the list
#call save_file function

def add_task(title):
    tasks = load_file()
    time = datetime.now().isoformat()
    if tasks:
        highest_id = max(task["id"] for task in tasks)
        task_id = highest_id + 1
    else: 
        task_id = 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "created_at": time,
        "updated_at": None
    }
    
    tasks.append(new_task)
    
    save_file(tasks)
    print("Task addded")
    return
    
#update
#given the id and title from main.py, loop through the loaded list and find the ID match
#check held ID with each ID from each dictionary
#when it matches, assign the passed title to the task "title" key of the dictionary. 
#call save_file function.

#if we finish the loop with no match. print "No matching task with given ID" and return. 


def update_task(id_number, new_title):
    tasks = load_file()
    current_time = datetime.now().isoformat()
    for task in tasks:
        if task["id"] == id_number:
            task["title"] = new_title
            task["updated_at"] = current_time
            
            save_file(tasks)
            return 
        
    print("No matching task found") 
            
    

#delete
#given argument from main.py, loop through the loaded list and find the ID match
#when the ID Matches, remove the task from the list with the remove() method.
#call save_file function.


def delete_task(id_number):
    id_number = int(id_number)
    tasks = load_file()
    
    for task in tasks:
        if task["id"] == id_number:
           tasks.remove(task)
           save_file(tasks)
           id_number = str(id_number)
           print("Task " + id_number + " deleted")
           return
           
           
    print("No matching task with given ID")
 


#list
#call function load_file
# print the list of tasks in a readable format.

def list_all():
    
    tasks = load_file()

    if not tasks:
        print("No tasks found")
        return
         
         
    for task in tasks:
        print(f"""
        ID: {task['id']}
        Title: {task['title']}
        Created: {task['created_at']}
        Updated: {task['updated_at']}
        """)  

    return  print(tasks)