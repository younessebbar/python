header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
todos = []
completed = []
help = """
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
"""
print(header)

while True:
    print("*" * 33)
    print("Enter a command. Type h for help: ")
    command = input("> ")
    if command == "q":
        break
    elif command == "h":
        print(help)
    elif command.isdigit() and len(todos) < int(command):
        print("I don't know that todo number")
    elif command.isdigit() and len(todos) >= int(command):
        done_todo = todos.pop(int(command) - 1)
        completed.append(done_todo)
    else:
        todos.append(command)
    for idx in range(len(todos)):
        print(f"{idx + 1}) {todos[idx]}")


if completed:
    print(f"Today you completed {len(completed)} todos:")
    for todo in completed:
        print(f"* {todo}")



