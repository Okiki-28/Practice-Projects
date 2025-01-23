import time

class todo:

    all_lists = []

    def __init__(self, name):
        self.name = name
        self.items = []
        self.count = 0
        todo.all_lists.append(name)

    def view_items(self):
        print(f"\n--{self.name}--")
        screen("\n------------------")
        if self.count == 0:
            screen("This list has no items")
        else:
            for i, item in enumerate(self.items):
                screen(f" ->{i+1}. {item}")
        screen("------------------\n")
        return self.items

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            self.count += 1
        else:
            print(f"{item} is already in this list")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.count -= 1
        else:
            screen(f"'{item}' is not in this list")

    def __str__(self):
        iden = "items"
        if self.count == 1:
            iden = "item"
        return f"{self.name} -> {self.count} {iden}"

    

def screen(text, end="", dy=1): #dy = delay
    for char in text:
        print(char, end="")
        time.sleep(dy/50)
    if not end == None:
        print(end)



def new_list():
    screen("\n-------")
    screen("Name of list: ", end=None)
    name = input()
    list1 = todo(name)
    
    add_items(list1)
    screen(f"\nList '{name}' has been created!")
    screen("\n----------------\n")

    return list1

def add_items(l):
    screen("How many items do you want to add: ", end=None)
    n = input()
    if not n.isdigit():
        screen("Invalid, enter integer: ", dy=0.1, end=None)
        n = input()
    n = int(n)
    for i in range(1, n+1):
        screen(f"  item {i}: ", end=None)
        l.add_item(input())
    screen("\n--Items have been added to list--")
    print()

def remove_items(l):
    screen("How many items do you want to remomve: ", end=None)
    while True:
        n = input()
        if not n.isdigit():
            screen("Invalid, enter integer: ", dy=0.1, end=None)
            continue
        elif int(n) > l.count:
            screen(f"Invalid, not up to {n} items in this list")
            screen("Enter no of items: ", end=None)
            continue
        break

    items = l.view_items()
    arr = []
    n = int(n)
    for i in range(1, n+1):
        screen(f"  Remove item: ", end=None)
        arr.append(int(input())-1)
    item_list = [items[i] for i in arr]
    for item in item_list:
        l.remove_item(item)
    screen("\n--Items have been removed from list--")

def view_list(l):
    print()
    if len(l) == 0:
        screen("You have no lists")
    else:
        screen("Viewing Saved lists")
        screen("===========")
        for i,lst in enumerate(l):
            screen(f"  {i+1}. {lst}")
    screen("\n----------------\n")
    time.sleep(len(l)//2)

def update_list(l):
    view_list(l)
    screen("List number: ", end=None)
    list1 = input()
    while not list1.isdigit():
        print("Invalid")
        screen("List number: ", end=None)
        list1 = input()
        
    list1 = l[int(list1)-1]
    screen(f"Updating {list1.name}...\n")
    while True:
        screen("--Menu--\n")
        screen("-> View Items [V]")
        screen("-> Add Items [A]")
        screen("-> Remove Items [R]")
        screen("")
        screen("-> Save List [X]")
        print()

        screen("Option: ", end=None)
        choice = input().upper()
        while choice not in ['V', 'A', 'R', 'X']:
            print("Invalid")
            choice = input("Option: ").upper()
    
        match choice:
            case 'V':
                list1.view_items()
            case 'A':
                add_items(list1)
            case 'R':
                remove_items(list1)
            case 'X':
                break
        screen(f"Will you like to perform more actions on '{list1.name}' [Y/N]: ", end=None)
        if not input().upper() == 'Y':
            print()
            break
        print()

def delete_list(l):
    view_list(l)

    screen("Which will you like to delete: ", end=None)
    i = input()
    
    if not i.isdigit():
        screen("Invalid, enter integer: ", dy=0.1, end=None)
        i = input()
    i = int(i)-1

    screen(f"'{l[i].name}' has been deleted")
    screen("\n-----------------------\n")
    del l[i]
    
    return l

    
def options():
    screen("Main Menu\n===========")
    screen("-> New List [N]")
    screen("-> All Lists [A]")
    screen("-> Update List [U]")
    screen("-> Delete List [D]")
    screen("")
    screen("-> End Session [X]")

    screen("\nOption: ", end=None)
    choice = input().upper()
    while choice not in ['N', 'A', 'U', 'D', 'X']:
        print("Invalid")
        choice = input("Option: ").upper()

    return choice

def main():
    screen("WELCOME TO YOUR TODO LIST PROGRAM\n")
    x = todo("Craig")
    y = todo("Nami")
    todo_list = [x, y]
    while True:
        choice = options()
        match choice:
            case 'N':
                todo_list.append(new_list())
            case 'A':
                view_list(todo_list)
            case 'U':
                update_list(todo_list)
            case 'D':
                todo_list = delete_list(todo_list)
            case 'X':
                break

main()








