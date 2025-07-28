camel = input("camelCase: ").strip()

snake=""
for i in camel:
  if i.isupper():
    snake+="_" +i.lower()
  else:
    snake+=i


print(f"snake_case: {snake}")
