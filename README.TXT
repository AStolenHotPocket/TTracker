A monkey brain CLI task manager written in python

Tasks are stored in a JSON file, they can be updated, deleted and listed from the terminal. 

Python 3
Run commands through main.py

Add a task:
python main.py add "task title"

Update a task:
python main.py update 1 "new title"

Delete a task:
python main.py delete 1

List all tasks:
python main.py list

Each task contains:

id:
title:
created at:
updated at: