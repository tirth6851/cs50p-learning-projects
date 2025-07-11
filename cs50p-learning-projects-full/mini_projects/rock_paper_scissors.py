import random

def get_computer_choice():
    #Randomly return 'rock', 'paper', or 'scissors'.
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    #Prompt the user until they enter a valid choice.
    valid = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in valid:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(player_choice, computer_choice):
    """
    Decide the winner.
    Returns:
      - 'tie'      if choices are the same,
      - 'player'   if the player wins,--------
      - 'computer' if the computer wins.
    """
    
    
    if player_choice == computer_choice:
        return 'tie'
    



    # Define which choice beats which
    winning_pairs = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    



    if winning_pairs[player_choice] == computer_choice:
        return 'player'
    else:
        return 'computer'

def main():
    print("Welcome to Rock–Paper–Scissors!")
    

    # Get both choices
    player = get_player_choice()
    computer = get_computer_choice()
    


    # Show what each chose
    print(f"You chose:     {player}")
    print(f"Computer chose: {computer}")
    




    # Determine and announce the result
    result = determine_winner(player, computer)
    if result == 'tie':
        print("It’s a tie!")
    elif result == 'player':
        print("You win!")
    else:
        print("Computer wins!")





if __name__ == "__main__":
    main()
