<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge" alt="CLI"> <img src="https://img.shields.io/badge/Dependencies-None-success?style=for-the-badge" alt="No dependencies"> <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT"> </p>

ToDoList is a simple, readable Python script that offers an interactive menu for adding, displaying, deleting, and clearing daily tasks. No external libraries, no installation, no complexity — just Python and your terminal.

---
###
✨ Features
###
| Feature | Description |  
| --- | --- |  
| ➕ Add Task | Add a new task with validation against empty input |  
| 📄 Show Tasks | Display a numbered list of all tasks |  
| 🗑 Delete Task | Remove by number, with type and range checks |  
| 🧹 Clear Tasks | Bulk-remove tasks after user confirmation |  
| 🚪 Safe Exit | Close the program through the menu |  
| 🛡 Error Handling | Prevents invalid input and actions on an empty list |  

---

No pip install required.

---

###
🖥 Sample Run
###

****** Managing Daily Routin ******
1. Add Task
2. Show Task
3. Delete Task
4. Clear Task
5. Exit
Your choice: 1
New Topic: Study a book
Successfully Added.

Your choice: 2

****** Tables of Tasks ******
1.Study a book

---

###
🧠 Code Structure
###

ToDoList.py
├── tasks = []          # global list storing tasks
├── add_task()          # add a task with input validation
├── show_task()         # display numbered tasks
├── delete_task()       # delete with try/except and range checks
├── clear_task()        # clear all tasks with user confirmation
└── while True: ...     # main menu loop

---
###
📌 Notes & Limitations
###

Data lives in memory only and is lost when the program exits.
The interface is command-line (CLI) and in English.
⚠️ Note: the clear_task function currently prompts itself again instead of clearing the list; this behavior will be fixed in a future release.

---
###
🗺 Roadmap
###

Persistent storage in a JSON file
Mark tasks as "done"
Fix the clear function and status messages
Add due dates and priorities
Graphical interface (Tkinter)

 ---
 ###
 🤝 Contributing
 ###

Contributions are welcome!

Fork the project.
Create a branch: git checkout -b feature/amazing
Commit your changes: git commit -m "Add amazing feature"
Push and open a Pull Request.
 Persistent storage in a JSON file
 Mark tasks as "done"
 Fix the clear function and status messages
 Add due dates and priorities
 Graphical interface (Tkinter)
