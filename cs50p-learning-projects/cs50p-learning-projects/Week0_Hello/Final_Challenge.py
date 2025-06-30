def ask():
  name = input("What's your name? ")
  age = input("How old are you? ")
  hobby = input("What's your favorite hobby? ")
  fcolor = input("What's your favorite color? ")
  dream = input("What's your biggest dream? ")
  return name, age, hobby, fcolor, dream

def main():
  name, age, hobby, fcolor, dream = ask()
  print()
  print(f"🧙‍♂️ Behold, the tale of {name}..." )
  print(f"At {age} years old, with a heart full of {fcolor}, {name} spends time {hobby}.")
  print(f"But deep inside, a dream awaits: {dream}.")
  print("Destiny whispers... 'soon' 🌌")

main()
