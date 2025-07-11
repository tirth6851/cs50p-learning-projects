from datetime import datetime
name = input("Name: ")
birth = int(input("Birth year: "))
fav = int(input("Favorite number: "))
age = datetime.now().year - birth
luck = fav * 7
print(f"\n🧙 {name}, age {age}, lucky stat is {luck}. Destiny awaits... 🌌")
