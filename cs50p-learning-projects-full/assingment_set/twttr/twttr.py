def main():

  text =users_input()
  print("Output: ",end="")
  for i in range(len(text)):
    if text[i] not in "aeiouAEIOU":
      print(f"{text[i]}", end="")
  print()



def users_input():
  return input("Input: ")

main()

