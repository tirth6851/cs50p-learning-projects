import sys



"""
you enter the name in the same command line used to run the file 
print("my name is",sys.argv[1])
"""




try:
  print("Hello,my name is",sys.argv[1])
except IndexError:
  print("not may words")

