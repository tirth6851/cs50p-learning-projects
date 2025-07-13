import sys

if len(sys.argv)<2:
  print(sys.exit("not may words"))
for arg in sys.argv:
  print("Hellow,my name is", arg)
print("Hellow,my name is",sys.argv[1])








"""
you enter the name in the same command line used to run the file 


------------------------------------------

try:
  print("Hello,my name is",sys.argv[1])
except IndexError:
  print("not may words")

  



------------------------------------------
if len(sys.argv)<2:
  print(sys.exit("not may words"))
elif len(sys.argv)>2:
  print(sys.exit("too many words"))


print("Hellow,my name is",sys.argv[1])


"""

