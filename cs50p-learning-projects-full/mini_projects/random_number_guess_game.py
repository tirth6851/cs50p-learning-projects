def main():
    import random
    secret_number = random.randint(1, 10)
    try_value=3

    print("I am thinking of a number between 1 and 10" )
    print("you have 3 trys")
    print("if you fail you lose you are not allowed to paly any gambling games")
    for i in range (1,4):
        if try_value <=3 :
            while True:
                try:
                    guess_of_user = int(input(print("what is your guess")))
                except ValueError:
                    print("that is not a number")
                else:
                    break
                    return guess_of_user
            if guess_of_user == secret_number:
                print("correct")
                break
            else:
                print("try again")
                try_value=+ 1
                if guess_of_user < secret_number:
                    print("too low")
                else:
                    print("too high")
        else:
            print("out of trys")




main()


