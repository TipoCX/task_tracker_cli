from sys import argv
from time import strftime
import json

def main():
    tasks: dict = {}

    #we try to read the file and loads the data to the tasks dict
    #if the file doesn't exists it creates the file and writes an empty dict
    try:
        tasks_file = open('tasks.json', 'r')
        if tasks_file:
            tasks = json.loads(tasks_file.read())
    except FileNotFoundError:
        tasks_file = open('tasks.json', 'w')
        tasks_file.write("{}")
    finally:
        tasks_file.close()

    #a simple write function to dump the dictionary into the json file
    def write():
        tasks_file = open('tasks.json', 'w')
        tasks_file.write(json.dumps(tasks))
        tasks_file.close()
        return

    #searches a free id based on the dict length and fills the object with the argument and default data
    if argv[1] == "add":
        free_id = len(tasks)
        while tasks.get(str(free_id))!=None:
            free_id+=1
        tasks[free_id] = {'description': argv[2], 'status': 'todo', 'createdAt': strftime("%d/%m/%G %X"), 'updatedAt': strftime("%d/%m/%G %X")}
        write()
        return


    #checks if the task exists and updates fields
    if argv[1] == 'update':
        if tasks.get(argv[2])!=None:
            tasks[argv[2]]['description'] = argv[3]
            tasks[argv[2]]['updatedAt'] = strftime("%d/%m/%G %X")
            write()
            return
        else:
            #in no object is found it warns the user through the console
            print("\nthe provided id doesn't exsists\n")
            return

    #similarly to the previous function, it checks if the id exsists and if so changes the status field
    if argv[1] == 'mark-in-progress':
        if tasks.get(argv[2])!=None:
            tasks[argv[2]]['status'] = 'in-progress'
            tasks[argv[2]]['updatedAt'] = strftime("%d/%m/%G %X")
            write()
        else:
            print("\nthe provided id doesn't exsists\n")
        return

    #similarly to the previous function it updates the status field
    if argv[1] == 'mark-done':
        if tasks.get(argv[2])!=None:
            tasks[argv[2]]['status'] = 'in-done'
            tasks[argv[2]]['updatedAt'] = strftime("%d/%m/%G %X")
            write()
        else:
            print("\nthe provided id doesn't exsists\n")
        return

    #simply checks the provided id and deletes the task
    if argv[1] == 'delete':
        if tasks.get(argv[2])!=None:
            tasks.pop(argv[2])
            write()
        else:
            print("\nthe provided id doesn't exsists\n")
        return

    #O(n) checks the amount of arguments and shows the desired tasks
    if argv[1] == "list":
        if len(argv)>2:
            #if more than 2 arguments (file name and comand) checks which list is the user looking for
            if argv[2] == 'todo':
                for t in tasks.keys():
                    if tasks[t]['status'] == 'todo':
                        print(f'{tasks[t]['description']} is {tasks[t]['status']}')
                return
            elif argv[2] == 'in-progress':
                for t in tasks.keys():
                    if tasks[t]['status'] == 'in-progress':
                        print(f'{tasks[t]['description']} is {tasks[t]['status']}')
                return
            elif argv[2] == 'done':
                for t in tasks.keys():
                    if tasks[t]['status'] == 'done':
                        print(f'{tasks[t]['description']} is {tasks[t]['status']}')
                return
            else:
                print("check status requested")
            return
        else:
            #if no other argument is presented, it shows all tasks
            for t in tasks.keys():
                print(f'{tasks[t]['description']} is {tasks[t]['status']}')
            return

main()
