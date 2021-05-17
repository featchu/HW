menu = {
    "1": "Display shopping list",
    "2": "Add item",
    "3": "Delete item",
    "4": "Delete shopping list",
    "5": "Search the shopping list"
}
for item in menu:
    print(item)
    print(menu[item])
item = input("\n Enter a number from the menu: ")

if item in menu:
    print(menu[item])
else:
    print(f"{item} was not found")
