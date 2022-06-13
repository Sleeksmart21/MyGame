import random

while True:
    my_action = input("Enter a choice (Rock, Paper, Scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {my_action}, computer chose {computer_action} .\n")

    while True:
       if computer_action=='rock' and my_action=='rock' or computer_action=='paper' and my_action=='Paper'or computer_action=='scissors' and my_action=='scissors':
               print('Draw!')
               break
       elif computer_action=='rock' and my_action=='Paper'or computer_action=='paper' and my_action=='scissors'or computer_action=='scissors' and my_action=='R':
               print('You Win!!!')
               break
       else:
               print('You Lose!!!')
               break        
