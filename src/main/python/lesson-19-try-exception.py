
try:
    number = int(input("Enter a number : "))
    print(number/0)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
