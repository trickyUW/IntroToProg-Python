# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PChuoy,8.2.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None  # An object for text file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # A string for user task
strPriority = ""  # A string for priority of task


# -- Processing -- #
# Step 1 - When the program starts, load any data you have in a text file
# called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
# Loop through strings in text file
for row in objFile:
    # Split task and priority by comma and make into list with 2 elements
    lstRow = row.split(",")
    # Add list elements into a dictionary with values of task and priority
    dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)  # Add dictionary into current list table
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority\n")
        # Loop through each dictionary in current list table
        for item in lstTable:
            # Get the task and priority of the dictionary and print them
            print(item["Task"] + " | " + item["Priority"])

        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # While loop for if user wants to add multiple items
        while (True):
            strTask = str(input("What task do you want to add? ")).strip()
            strPriority = str(input("What is the priority of the task? (High|Medium|Low) ")).strip()
            lstTable.append({"Task": strTask, "Priority": strPriority})

            # Stop adding items if user does not enter 'y'
            strChoice = input("Continue adding tasks? ('y/n') ")
            if strChoice.lower() != 'y':
                break

        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # While loop for if user wants to delete multiple items
        while (True):
            blnFoundFlag = False  # Flag for dealing with duplicates
            strTask = input("What task do you want to delete? ")
            # Loop through each dictionary in current list table
            for item in lstTable:
                # If task is in list table, delete
                if item["Task"].lower() == strTask.lower():
                    lstTable.remove(item)
                    print("Task deleted")
                    blnFoundFlag = True

            # Task is not found in list table
            if not blnFoundFlag:
                print("Task does not exist in the list")

            # Stop deleting items if user does not enter 'y'
            strChoice = input("Continue deleting tasks? ('y/n') ")
            if strChoice.lower() != 'y':
                break

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        # Loop through each dictionary in current list
        for row in lstTable:
            # Write to file (task,priority)
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("Tasks saved to file.")

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program

input("\nPress Enter to exit the program ")