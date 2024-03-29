# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

#Function for registering a user
def reg_user():
            '''Add a new user to the user.txt file'''
            while True:
                # - Request input of a new username
                new_username = input("New Username: ")
            
                #Checking if the user exists
                if new_username not in username_password.keys():
                    #Requesting new password
                    while True:
                        # - Request input of a new password
                        new_password = input("New Password: ")

                        # - Request input of password confirmation.
                        confirm_password = input("Confirm Password: ")

                        # - Check if the new password and confirmed password are the same.
                        if new_password == confirm_password:
                            # - If they are the same, add them to the user.txt file,
                            print("New user added")
                            username_password[new_username] = new_password
            
                            with open("user.txt", "a+") as out_file:
                                user_data = []
                                for k in username_password:
                                    user_data.append(f"{k};{username_password[k]}")
                                    out_file.write("\n".join(user_data))
                            break
                        # - Otherwise you present a relevant message.
                        elif new_password != confirm_password:
                            print("\nPasswords do no match\n")
                            break
                else:
                    print("\nUser exists. Please choose different name.\n")
                break

#Function for adding a user                    
def add_task():
            '''Allow a user to add a new task to task.txt file
                Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.'''
            task_username = input("Name of person assigned to task: ")
            if task_username not in username_password.keys():
                print("User does not exist. Please enter a valid username")
                
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break

                except ValueError:
                    print("Invalid datetime format. Please use the format specified")


            # Then get the current date.
            curr_date = date.today()
            ''' Add the data to the file task.txt and
                Include 'No' to indicate if the task is complete.'''
            new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": False
            }

            task_list.append(new_task)
            with open("tasks.txt", "w") as task_file:
                task_list_to_write = []
                for t in task_list:
                    str_attrs = [
                        t['username'],
                        t['title'],
                        t['description'],
                        t['due_date'].strftime(DATETIME_STRING_FORMAT),
                        t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if t['completed'] else "No"
                    ]
                    task_list_to_write.append(";".join(str_attrs))
                task_file.write("\n".join(task_list_to_write))
            print("Task successfully added.")

#Function for viewing all tasks
def view_all():
            '''Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling) 
            '''

            for t in task_list:
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)

#Function for viewing current users tasks
def view_mine():
            '''Reads the task from task.txt file and prints to the console in the 
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling)
            '''
            #Reads through tasks
            for index, t in enumerate(task_list):
                if t['username'] == curr_user:
                    #Display the task that belongs to current user
                    disp_str = f"Task Number: \t {index}\n" 
                    disp_str += f"Task: \t\t {t['title']}\n" 
                    disp_str += f"Assigned to: \t {t['username']}\n"
                    disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    disp_str += f"Task Description: \n {t['description']}\n"
                    #Prints each task with an a corresponding index
                    print(disp_str)
            
            #User selects task which they want to edit
            task_no = input("Enter a task number to modify it or enter -1 to return to the menu: ")
            task_no = int(task_no)
            if task_no >= 0:
                user_response = input("Would you like to edit this task or mark it as complete (edit/mark):")
                if user_response == "edit":
                    user_edit = input("Would you like to change the username or due date (username/date):")
                    if user_edit == "username":
                        new_name = input("Enter the new username:")

                        list_of_tasks = []
                        new_list = []
                        with open("tasks.txt", "r+") as file:
                            for line in file.readlines()[task_no]:
                                list_of_tasks.append(line)

                        x = ""
                        for i in list_of_tasks:
                            if i == task_list[0]:
                                new_list.append(new_name)
                            else:
                                new_list.append(x)

                        with open("tasks.txt", "r+") as file:
                            for i in new_list:
                                file.write(i)    

                    elif user_edit == "date":
                        new_date = input("Enter the new date: yyyy/mm/dd")
                        list_of_tasks = []
                        new_list = []
                        with open("tasks.txt", "r+") as file:
                            for line in file.readlines()[task_no]:
                                list_of_tasks.append(line)

                        x = ""
                        for i in list_of_tasks:
                            if i == task_list[3]:
                                new_list.append(new_date)
                            else:
                                new_list.append(x)

                        with open("tasks.txt", "r+") as file:
                            for i in new_list:
                                file.write(i)

                elif user_response == "mark":
                    list_of_tasks = []
                    new_list = []
                    with open("tasks.txt", "w+") as file:
                        for line in file.readlines()[task_no]:
                            list_of_tasks.append(line)

                    x = ""
                    for i in list_of_tasks:
                        if i == "No":
                            new_list.append("Yes")
                        else:
                            new_list.append(x)

                    with open("tasks.txt", "w+") as file:
                        for i in new_list:
                            file.write(i)
                    
            else:
                pass

#Function to generate reports
def generate_reports():
        # Create task_overview.txt if it doesn't exist
        if not os.path.exists("task_overview.txt"):
           file = open("task_overview", "w") 

        completed_tasks = []
        incompleted_tasks = []
        overdue_tasks = []

        #Reads through task list and appends all completed tasks into a new list
        for i in task_list:
            if i["completed"] == True:
                completed_tasks.append(i)
        
        #Reads through task list and appends all incompleted tasks into a new list
        for i in task_list:
            if i["completed"] == False:
                incompleted_tasks.append(i)

        #Reads through task list and appends all incompleted and overdue tasks into a new list
        for i in task_list:
            if i["completed"] == False and datetime.now() > i["due_date"]:
                overdue_tasks.append(i)        

        #Calculation for percentages 
        percentage_of_incompleted_tasks = (len(incompleted_tasks) / len(task_list)) * 100
        percentage_of_overdue_tasks = (len(overdue_tasks) / len(task_list)) * 100

        #Writes user reports (task percentages) into file
        file.write("Total number of tasks:" + str(len(task_list)))
        file.write("\n")
        file.write("Total number of completed tasks:" + str(len(completed_tasks)))
        file.write("\n")
        file.write("Total number of incompleted tasks:" + str(len(incompleted_tasks)))
        file.write("\n")
        file.write("Total number of overdue incompleted tasks:" + str(len(overdue_tasks)))
        file.write("\n")
        file.write("Percentage of incompleted tasks:" + str(percentage_of_incompleted_tasks))
        file.write("\n")
        file.write("Percentage of overdue tasks:" + str(percentage_of_overdue_tasks))
        file.close()

        # Create user_overview.txt if it doesn't exist
        if not os.path.exists("user_overview.txt"):
            file = open("user_overview.txt", "w") 
        
        file.write("Total number of users: " + str(len(username_password.keys())))
        file.write("\n")
        file.write("Total number of tasks:" + str(len(task_list)))

        #Reads through task list and appends all completed tasks into a new list per user
        for i in user_data:
            comp_task = []
            if curr_t["completed"] == True:
                for x in task_list:
                    comp_task.append(x)
        
        #Reads through task list and appends all incompleted tasks into a new list per user
        for i in user_data:
            incomp_task = []
            if curr_t["completed"] != True:
                for x in task_list:
                    incomp_task.append(x)

        #Reads through task list and appends all incompleted and overdue tasks into a new list per user
        for i in user_data:
            overdue_incomp_task = []
            if curr_t["completed"] != True and datetime.today() > curr_t["due_date"]:
                for x in task_list:
                    overdue_incomp_task.append(x)

        #Writes user reports (task percentages) into file for each user 
        for i in user_data:
            file.write("Total assigned tasks: " + str(len(task_list)))
            file.write("\n")
            file.write("Percentage of assigned tasks: " + str((len(task_list) / len(task_list)) * 100))
            file.write("\n")
            file.write("Percentage of completed assigned tasks: " + str((len(comp_task) / len(task_list)) * 100))
            file.write("\n")
            file.write("Percentage of incompleted assigned tasks: " + str((len(incomp_task) / len(task_list)) * 100))
            file.write("\n")
            file.write("Percentage of incompleted and overdue assigned tasks: " + str((len(overdue_incomp_task) / len(task_list)) * 100))

        file.close()

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    #Only shows ds option when the user is admin
    if curr_user == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    e - Exit
    : ''').lower()
    
    #Function to register a user is called if  the user enters "r"
    if menu == 'r':
        reg_user()
    
    #Function to add a task is called if  the user enters "a"
    elif menu == 'a':
        add_task()

    
    #Function to view all tasks is called if the user enters "va"
    elif menu == 'va':
        view_all() 
    
    #Function to view all current tasks is called if the user enters "vm"
    elif menu == 'vm':
        view_mine()
     
    #Function to generate reports is called when user enters "gr"
    elif menu == "gr":
        generate_reports()        
    
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")