print("Welcome to the Calculator.")
operation = ["Add", "Subtract", "Multiply", "Divide", "Power"]
a = input(operation)
#intialize the operations
def calculator():
    if a == "add":
        add1 = int(input("Enter a number"))
        add2 = int(input("Enter a number"))
        answeradd = (print(add1 + add2))
    if a == "subtract":
        sub1 = int(input("Enter a number"))
        sub2 = int(input("Enter a number"))
        answersub = (print(sub1 - sub2))
    if a == "multiply":
        multiply1 = int(input("Enter a number"))
        multiply2 = int(input("Enter a number"))
        answermultiply = (print(multiply1 * multiply2))
    if a == "divide":
        div1 = int(input("Enter a number"))
        div2 = int(input("Enter a number"))
        answerdiv = (print(div1 / div2))
    if a == "power":
        power1 = int(input("Enter a number"))
        power2 = int(input("Enter a number"))
        answerpower = (print(power1 ** power2))
#intialize the calculator
calculator()