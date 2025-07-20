from random import choice 
import random 


'''
coin = choice(["heads","tails"])
#print(coin)
for i in coin:
  print(coin)
------------------------------------
  

number = random.randint(1,10)
print(number)
------------------------------------
'''

cards =["jack","queen","king"]
random.shuffle(cards)
for i in cards :
  print(i)