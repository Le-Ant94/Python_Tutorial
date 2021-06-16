#try-except allows you to excecute the rest of the code to run if there is an error in a piece of code

try:
    number = int(input("Enter a number: \n"))
    result = number / 0
    print(result)
except:
    print("Invalid input")
