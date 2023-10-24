#ToDoList, the first project that makes me work with lists (arrays) and makes me use a for loop.

toDoList = []

def viewList (toDoList):
    for i, item in enumerate(toDoList, start=1):
        print((i), (item))

def appendList (toDoList, prompt):
   
    toDoList.append(input(prompt))
    print ('\n' + "Your updated list:" + '\n')
    viewList(toDoList)
    return toDoList

def deleteItem(toDoList):
    
    while True:
        print('\n'+"What would you like to delete? Here is your list: " + '\n')
        viewList(toDoList)

        try:
            sup = int(input('\n'+"Enter the number corresponding to your list item: " + '\n')) - 1
        

            if 0 <= sup < len(toDoList):
                del toDoList[sup]
                return toDoList
            else:
                print('\n'+"This is not an item on the list " + '\n')

        except ValueError:
            print ('\n'+"Please enter a number!" + '\n')
            continue



appendList(toDoList, '\n'+"Enter your next to-do list element below " + '\n')

while True:
    while True:
        q = input('\n'+"Would you like to add another item to the list? (Y/N) " + '\n' + '\n')
        if q.upper() == 'N':
            break
        elif q.upper() == 'Y':
            appendList(toDoList, '\n'+"Enter your next to-do list element below " + '\n')
            

    while True:
        q2 = input('\n' + "To see list type: S" + '\n' + "To delete an list item type: D" + '\n' + 
        "To add another item type : A" + '\n' +
        "To exit the application type: E" + '\n')
        if q2.upper() == 'S':
            viewList(toDoList)
        elif q2.upper() == 'D':
            deleteItem(toDoList)
        elif q2.upper() == 'A':
            appendList(toDoList, '\n'+"Enter your next to-do list element below " + '\n')
        elif q2.upper() == 'E':
            break
        else:
            print( '\n'+"Please enter a valid answer")
    break




