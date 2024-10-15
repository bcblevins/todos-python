is_running = True
is_taking_input = False

todos = []


new_todo = ''

menu = '''
What would you like to do?
--------------------------
1. Add new todo
2. Delete todo
3. Update todo
4. Quit
'''

# show menu, todos and take input
def show_menu():
    while is_taking_input:

        # get todos
        todos = []
        with open('todos.txt', 'r') as todos_file:
            for todo in todos_file:
                todos.append(todo)
        #print whole list of todos and menu
        for todo in todos:
            status = '[x] '
            if todo[0] == 'o':
                status = '[ ] '
            print(status + todo[1:])        
        print(menu)
        
        user_input = input()

        # validate choice, start loop over if not, if so return input
        choices = ['1','2', '3', '4']
        if user_input not in choices:
            print(user_input + 'is not a valid option')
            continue
        else:
            return user_input

def delete_todo():
    while True:
        count = 0

        # get todos
        todos = []
        with open('todos.txt', 'r') as todos_file:
            for todo in todos_file:
                todos.append(todo)

        # Give option to go back to main menu
        print('0. GO BACK')

        # Print todos with numbers
        for todo in todos:
            count += 1
            status = '[x] '
            if todo[0] == 'o':
                status = '[ ] '
            print(str(count) + '. ' + status + todo[1:])
        print('Select the number for the todo you\'d like to delete')
        choice = input()

        # Go back to main menu if 0 chosen
        if choice == '0':
            break

        # Validate if int
        try:
            todo_to_delete = int(choice)
        except ValueError:
            print(choice + " is not a number")
            continue

        # Validate choice
        if todo_to_delete > len(todos) or todo_to_delete < 1:
            print(choice + " is not once of the options")
            continue
        else:
            todos.pop(todo_to_delete - 1)

        # Rewrite todo file with update to todo list
        with open("todos.txt", "w") as todos_file:
            for todo in todos:
                todos_file.write(todo)
            
            

# Start loop
while is_running:
    is_taking_input = True
    choice = show_menu()
    if choice == '1':
        print('Input new todo:')
        new_todo = 'o' + input()
        with open('todos.txt', 'a') as todos_file:
            todos_file.write('\n' + new_todo)
    elif choice == '2':
        delete_todo()
    elif choice == '4':
        is_running = False
        print('Goodbye')
        break
        















        
