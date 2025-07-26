math=input("Expression: ")

x, y, z = math.split(" ")



'''
x is the fist value user gives
y is the what to do likke add, minis and etc
z is the last number
'''

x=float(x)
z=float(z)

if y == "+":
  print(f"{x+z}")
elif y == "-":
  print(f"{x-z}")
elif y == "*":
  print(f"{x*z}")
elif y == "/":
  print(f"{x/z}")
else:
  print("invalid sing")
