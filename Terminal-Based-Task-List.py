import subprocess
from pathlib import Path

#get program's location and define path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
user_list = script_dir / "user_list.txt"

print("Welcome to Terminal Based Task List (TBTL)")
print("Please read the README for instructions")

while True:
    print("\nOpen list[1] Quick View Tasks[2] Quick add task[3] Quick mark task[4] Exit Program[5]")
    user_input = input("Enter a number: ")

    try:
        #open List
        if user_input == '1':
            try:
                #Tries to open file
                with open(user_list, 'r'):
                    print("File found, opening file through nano...")
            except FileNotFoundError:
                # If it doesn't exist, create it
                with open(user_list, 'w') as f:
                    pass
                print("Created new task list, opening file through nano...")

            #open the file in nano
            subprocess.run(["nano", str(user_list)])

        #quick view List
        elif user_input == '2':
            with open(user_list, 'r') as file:
                print(file.read())
        
        #quick add task
        elif user_input == '3':
            with open(user_list, 'a') as file:
                user_input = input("Input new task: ")
                file.write(user_input + "\n")
        
        #quick mark task
        elif user_input == '4':
            #print file
            with open(user_list, 'r') as file:
                print(file.read())

            user_input = input('Input task: ')
            uniform_user_input = " ".join(user_input.split()).casefold()

            match = False
            updated_tasks = []

            #read and check for task
            with open(user_list, 'r') as file:
                for task in file:
                    stripped_task = task.rstrip('\n')
                    uniform_task = " ".join(stripped_task.split()).casefold()
                    
                    if uniform_user_input == uniform_task:
                        match = True
                        #add delete marker ($Done)
                        updated_tasks.append(f"{stripped_task} $Del\n")
                    else:
                        updated_tasks.append(task)

            #if a match was found, rewrite the file with the updates
            if match:
                with open(user_list, 'w') as file:
                    file.writelines(updated_tasks)
                print("Lines marked")
            else:
                print("Error: No match found")
     
        elif user_input == '5':
            #delete marked tasks
            with open(user_list, 'r'):
                tasks = file.readlines()
            
            with open(user_list, 'w'):
                for task in tasks:
                    if "$Done" not in task:
                        file.write(task)

            print("Changes saved, exiting...")
            break
            
    except Exception as e:
        print(f"An error occurred: {e}")