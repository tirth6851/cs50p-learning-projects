import random
ans = random.randint(1,100)
guess = None
while guess != ans:
    guess = int(input("Guess (1–100): "))
    if guess < ans:
        print("Too low!")
    elif guess > ans:
        print("Too high!")
print("Correct!")
