try:
    x = int(input("Numerator: "))
    y = int(input("Denominator: "))
    print(x / y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
