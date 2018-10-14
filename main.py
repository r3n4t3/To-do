from enum import Enum
import datetime


class ToDo:

    def __init__(self, id, title, status, date):
        self.id = id
        self.set_title(title)
        self.set_status(status)
        self.set_date(date)

    def set_title(self, title):
        if len(title) > 0:
            self.title = title
        else:
            raise ValueError("Task title cannot be empty")

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def __str__(self):
        return (str( self.id ) + ". " + self.title + "\t|\t" + self.status.name + "\t|\t" + self.date.strftime("%Y-%m-%d"))


class Status(Enum):
    COMPLETED = 1
    PENDING = 2
    CANCELED = 3

def assemble_date(year, month, day):
    return datetime.date(year, month, day)

def print_menu():
    print("Select an option from the menu below :")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Get all tasks")
    print("4. Get today's task")
    print("5. Delete a task")
    print("6. Exit")

def print_status():
    print("Selection a status for your new task :")
    print("1. COMPLETED")
    print("2. PENDING")
    print("3. CANCELED")
    return input(" : ")

def analyze_status():
    status = print_status()
    if status == '1':
        return Status.COMPLETED
    elif status == '2':
        return Status.PENDING
    elif status == '3':
        return Status.CANCELED
    else:
        print("Invalid option, try again.!\n\n")
        return Status.PENDING

def analyze_option(option):
    print("\n")
    if option == '1':
        task_title = input("Enter the title of the task : ")
        task_status = analyze_status()
        date_entry = input("Enter a date in YYYY-MM-DD format : ")
        year, month, day = map(int, date_entry.split('-'))
        task_date = assemble_date(year, month, day)
        to_do = ToDo(len(to_do_list), task_title, task_status, task_date)
        to_do_list.append(to_do)
        print("Added task.")
        print()
    elif option == '2':
        print("Updated task.")
    elif option == '3':
        print("All Tasks : ")
        for to_do in to_do_list:
            print(to_do)
        print()
    elif option == '4':
        print("Today's task : ")
        count = 1
        for to_do in to_do_list:
            if to_do.get_date().strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d"):
                print(count + ". " +to_do)
        print()
    elif option == '5':
        id = input("Enter task id : ")
        for to_do in to_do_list:
            if str( to_do.get_id() ) == id:
                to_do_list.remove(to_do)
                exit
        print ("Deleted tasks.")

    elif option == '6':
        print ("Good Bye! ~\0/~")
        exit()
    else:
        print(chr(27) + "[1J")
        print("Invalid option, try again.!\n\n")

to_do_list = []
if __name__ == '__main__':
    print("\nWelcome to your to-do app!...\n")
    while True:
        print_menu()
        analyze_option(input(" : "))