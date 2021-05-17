name = input("Write your name:")
text = input("Write a text (characters or numbers):")
if text.isdigit():
    print(f" The text made out of numbers was found by {name}.")
else:
    print(f" The text made out of characters was found by {name}.")
