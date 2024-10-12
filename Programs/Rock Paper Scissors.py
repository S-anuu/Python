import random

options = ( 'rock', 'paper', 'scissors')
running = True

while running:
    player = None
    computer = random.choice(options)

    player = input('Enter a choice (rock, paper, scissors): ').lower()

    while player not in options:
        print('It is not a valid choice.')
        player = input('Enter a choice (rock, paper, scissors): ').lower()
    
    print(f'Player: {player.capitalize()}')
    print(f'Computer: {computer.capitalize()}')

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win! :)")
    elif player == "scissors" and computer == "paper":
        print("You win! :)")
    elif player == "paper" and computer == "rock":
        print("You win! :)")
    else:
        print("You lose :(")

    if not input('Play again? (y/n): ').lower() == "y":
        running = False

print('Thanks for playing!')