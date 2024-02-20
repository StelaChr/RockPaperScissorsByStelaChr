from random import randint
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
trials_counter = 0
win_counter = 0
lose_counter = 0

while True:
    player_move = input (Fore.WHITE + f"You have {3 - trials_counter} trials left. Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print (Fore.MAGENTA + "Invalid Input. Try again...")
        continue
    if not player_move!= "r" or player_move!= "s" or player_move!= "p" :
        trials_counter += 1
    computer_random_number = randint (1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print (Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        print (Fore.GREEN + "You win!")
        win_counter+=1
    elif player_move == computer_move:
        print (Fore.YELLOW + "Draw!")
    else:
        print (Fore.RED + "You lose!")
        lose_counter+=1

    if win_counter==3:
        print (Fore.GREEN + "Well done! You won 3 of 3! Do you want to play one more time? Y/N: ")
        player_choice = input()
        if player_choice == "Y":
            trials_counter = 0
            win_counter = 0
            lose_counter = 0
        elif player_choice == "N":
            print ("Thanks for playing! Goodbye!")
            break
    elif lose_counter==3:
        print (Fore.RED + "Sorry! You lost 3 of 3! Do you want to play one more time? Y/N: ")
        player_choice = input()
        if player_choice == "Y":
            trials_counter = 0
            win_counter = 0
            lose_counter = 0
        elif player_choice == "N":
            print ("Thanks for playing! Goodbye!")
            break
    elif trials_counter == 3 and win_counter > lose_counter:
        print(Fore.GREEN + "Well done! You won! Do you want to play one more time? Y/N: ")
        player_choice = input()
        if player_choice == "Y":
            trials_counter = 0
            win_counter = 0
            lose_counter = 0
        elif player_choice == "N":
            print("Thanks for playing! Goodbye!")
            break
    elif trials_counter == 3 and win_counter < lose_counter:
        print(Fore.RED + "Sorry! You lost! Do you want to play one more time? Y/N: ")
        player_choice = input()
        if player_choice == "Y":
            trials_counter = 0
            win_counter = 0
            lose_counter = 0
        elif player_choice == "N":
            print("Thanks for playing! Goodbye!")
            break
    elif trials_counter == 3 and win_counter == lose_counter:
        print(Fore.YELLOW + "Draw! Do you want to play one more time? Y/N: ")
        player_choice = input()
        if player_choice == "Y":
            trials_counter = 0
            win_counter = 0
            lose_counter = 0
        elif player_choice == "N":
            print(Fore.LIGHTCYAN_EX + "Thanks for playing! Goodbye!")
            break


