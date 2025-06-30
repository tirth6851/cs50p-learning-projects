hour = int(input("What hour is it? (0–23) "))
if 5 <= hour < 12:
  print("Good morning!")
elif 12 <= hour < 17:
  print("Good afternoon!")
elif 17 <= hour < 22:
  print("Good evening!")
else:
  print("Good night!")
