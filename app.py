# write a code for print 'Hello World' in python
print('Hello World')

#create list of choice including rock, paper, scissor

choices = ['rock', 'paper', 'scissor']

#create a two variables for player and computer

player = None   #player choice
computer = None #computer choice

#create a winner variable for winner
winner = None

#create a while loop for run the game until user want to quit   
while True:
    #take input from user
    player = input('rock, paper or scissor?').lower()
    #import random module for computer choice
    import random
    #use random.choice() for computer choice
    computer = random.choice(choices)
    #check if the player and computer are same
    if player == computer:
        print('Tie')
    #check for rock
    elif player == 'rock':
        if computer == 'paper':
            print('Computer wins')
        else:
            print('You win')
    #check for paper
    elif player == 'paper':
        if computer == 'scissor':
            print('Computer wins')
        else:
            print('You win')
    #check for scissor
    elif player == 'scissor':
        if computer == 'rock':
            print('Computer wins')
        else:
            print('You win')
    #check if the player enter wrong choice
    else:
        print('Wrong choice')
    #ask user for play again
    play_again = input('Play again? (yes/no): ').lower()
    #if user want to play again
    if play_again != 'yes':
        break


