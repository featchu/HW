number = int(input("Enter a number: "))
if number > 0:
    if number < 10:
        print("{0} is positive and lower than 10".format(number))
    else:
        print("{0} is positive and higher than (or equal to) 10".format(number))
elif number == 0:
    print("The number is 0")
elif number < 0:
    print("The number was negative so now it's been converted into a positive one aka {0}".format(abs(number)))
