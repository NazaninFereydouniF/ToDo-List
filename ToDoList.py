tasks = []

#def add_ask(task):
    #tasks.append(task)

def add_task():
    task = input('New Topic: ').strip()

    if not task:
        print('Empty')
        return

    tasks.append(task)
    print('Successfully Added.')

def show_task():
    if not tasks:
        print('Empty! There is no task.')
        return

    print('\n****** Tables of Tasks ******')

    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task}")

def delete_task():
    if not tasks:
        print('Empty! There is no task for deleting.')
        return

    show_task()

    try:
        number = int(input('Please eneter number of the task for deleting: '))

    except ValueError:
        print('Invalid Number! \nPlease enter an integer number.')
        return

    if 1 <= number <= len(tasks):
        remove_task = tasks.pop(number - 1)
        
        print("Removed: ", remove_task)
        print(f"Task number {number} removed.")

    else:
        print('The number is invalid.')


def clear_task():
    if not tasks:
        print('The table of tasks is empty!')
        return
    
    confirmation = input('Are sure for deleting? Please enter "Y" or "N". ').strip()

    if confirmation == 'Y':
        clear_task()
        print('The selected task successfully deleted.')

    else:
        print('Empty! There is no task for deleting.')

while True:
    print('\n****** Managing Daily Routin ******')

    print('1. Add Task')
    print('2. Show Task')
    print('3. Delete Task')
    print('4. Clear Task')
    print('5. Exit')

    choice = input('Your choice: ')

    if choice == '1':
        add_task()

    elif choice == '2':
        show_task()

    elif choice == '3':
        delete_task()

    elif choice == '4':
        clear_task()

    elif choice == '5':
        #exit()
        print('Exit')
        break

    else:
        print('Not Valid Choice.')