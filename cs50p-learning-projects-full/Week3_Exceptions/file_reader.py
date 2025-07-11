try:
    filename = input("Filename: ")
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
