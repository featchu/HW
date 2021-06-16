# Adaugă categoriile dorite de la tastatură:

with open("categories.txt", 'a') as file:
    pass
# a => deschidem fisierul cu drept de adaugare,daca fisierul nu exista, il adauga
category = ""


# functie ptr verificarea existentei categoriilor in fisierul category
def check_categories(category: str):
    i = 0
    with open("categories.txt", 'r') as file:
        for new_category in file:
            if category == new_category:
                i += 1
        return i


# daca i != 0, new_category se afla in category
# daca i = 0, new_category nu se afla in category
# r => drepturi doar de citire,read-only

# functie ptr scrierea categoriilor in fisierul category
def write_item(category: str):
    while category != 'DONE':
        category = (input("Insert a task category: ")).lower()

        if category == 'DONE':
            break
        elif check_categories(category) != 0 or category.isspace() is True:
            # isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
            print("This category already exists")
        else:
            with open("categories.txt", 'a') as file:
                # a => deschidem fisierul cu drept de adaugare,daca fisierul nu exista, il adauga
                file.write(f"{category}\n")
        continue


# Se va cere de la tastatura, pe rand introducerea unui task de la tastatura

# functie ptr verificarea existentei task in fisierul task.txt
def check_task(task: str):
    i = 0
    with open("task.txt", 'r') as file2:
        for name in file2:
            if task == name:
                i += 1
        return i


# functie ptr scrierea taskurilor in fisierul task
def write_task(task: str):
    # ptr adăugarea ulterioara a categoriei din care taskul face parte
    category = (input("Select category: ")).lower()
    check_categories(category)
    while check_categories(category) == 0:
        category = (input("Category missing. Select another category: ")).lower()

    task = (input(f"Insert task for {category}: ")).lower()
    check_task(task)
    while task != 'DONE':
        task = (input("Insert task: ")).lower()
        if task == 'DONE':
            break
        elif check_categories(task) != 0 or task.isspace() is True:
            print("Task already exists.")
        else:
            print('Deadline: \n')
            year = int(input("  Year: "))
            month = int(input("\n  Month: "))
            day = int(input("\n  Day: "))
            hour = int(input("\n  Hour: "))
            minute = int(input("\n  Minute: "))
            person_in_charge = input("    Person in charge: ")
            with open("task.txt", 'a') as file2:
                # a => deschidem fisierul cu drept de adaugare,daca fisierul nu exista, il adauga
                file2.write(f"Category: {category} ,Date and time: {year}/{month}/{day} {hour}:{minute} Person in charge: {person_in_charge} {task}\n")
        continue


write_item(category)
write_task(task)
