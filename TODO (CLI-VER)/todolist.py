# Check for the existence of file
no_of_items = 0
try:
    f = open("./TODO (CLI-VER)/todolist.txt")
    p = 0
    for i in f.readlines():  # Counting the number of items if the file exists already
        p += 1
    no_of_items = p-2
except:
    f = open("./TODO (CLI-VER)/todolist.txt", 'w')
    f.write("_________TODO LIST__________\n")
    f.write("    TIME                   WORK")
finally:
    f.close()
# Todo list
print("Press 1: Add Item \nPress 2: Delete Item \nPress 3: Update item \nPress 4: Display Items\nPress 5: Exit")
n = int(input())
while n == 1 or n == 2 or n == 3 or n == 4:
    if n == 1:
        todo = []
        print("Enter the time in HH:MM format(24 hours format)")
        time = input()
        print("Enter your Work")
        work = input()
        no_of_items += 1
        with open('./TODO (CLI-VER)/todolist.txt', 'a') as f:
            f.write("\n"+str(no_of_items)+"    " +
                    time+"                   "+work)
    elif n == 2:
        if (no_of_items <= 0):
            print("There is no item in the list kindly add some items")
        else:
            print("____________________________________________________________")
            print("Your Current List: ")
            todo = []
            with open('./TODO (CLI-VER)/todolist.txt') as f:
                for i in f.readlines():
                    print(i)
                    todo.append(i)
            print("____________________________________________________________")
            print("Enter the position of the item you want to delete : ")
            pos = int(input())
            if (pos <= 0):
                print("Please enter a valid position")
            elif (pos > (no_of_items)):
                print("Please enter the position <= {}".format(no_of_items))
            else:

                todo.pop(pos+1)
                no_of_items -= 1
                if (no_of_items <= 0):
                    print("Congratulations your todo list is empty!")

                with open('./TODO (CLI-VER)/todolist.txt', 'w') as f:
                    for i in range(len(todo)):
                        if i >= (pos+1):
                            f.write(str(pos)+todo[i][1:])
                            pos += 1
                        else:
                            f.write(todo[i])

    elif n == 3:
        print("____________________________________________________________")
        print("Your Current List: ")
        todo = []
        with open('./TODO (CLI-VER)/todolist.txt') as f:
            for i in f.readlines():
                print(i)
                todo.append(i)
        print("____________________________________________________________")
        print("Enter the position of the items you want to update : ")
        pos = int(input())
        if (pos <= 0):
            print("Please enter a valid position")
        elif (pos > (no_of_items)):
            print("Please enter the position <= {}".format(no_of_items))
        else:
            print("What you want to update : ")
            print("Press 1: Time\nPress 2: Work")
            choice = int(input())
            if choice == 1:
                print("Enter your updated time :")
                time = input()
                p = todo[pos+1].index(":")
                y = 0
                with open('./TODO (CLI-VER)/todolist.txt', 'w') as f:
                    for i in range(len(todo)):
                        if i == pos+1:
                            f.write(str(pos)+"    "+time+"" +
                                    ''.join(todo[pos+1][p+3:]))
                        else:
                            f.write(todo[i])
            elif choice == 2:
                print("Enter your updated work :")
                work = input()
                p = todo[pos+1].index(":")
                y = 0
                with open('./TODO (CLI-VER)/todolist.txt', 'w') as f:
                    for i in range(len(todo)):
                        if i == pos+1:
                            f.write(
                                str(pos)+"    "+''.join(todo[pos+1][p-2:p+3])+"                   "+work)
                        else:
                            f.write(todo[i])
    elif n == 4:
        print("Your Current List: ")
        todo = []
        print("____________________________________________________________")
        with open('./TODO (CLI-VER)/todolist.txt') as f:
            for i in f.readlines():
                print(i)
                todo.append(i)
        print("____________________________________________________________")
    print("Press 1: Add Item \nPress 2: Delete the Item\nPress 3: Update item\nPress 4:Display Items\nPress 5:Exit")
    n = int(input())
print("Thank you for using our application")
