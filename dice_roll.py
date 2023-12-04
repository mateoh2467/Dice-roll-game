# get random number from library
from random import randint
computer_guess = 0
person_guess = 0
die_1 = 0
die_2 = 0
total_die = 0
results_part_1 = ""
results_part_2 = ""
play_again = ""
person_error = "0"
# create main function
def main():
    # computer and dice and total die random numbers
    computer_guess = randint(1, 6)
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    total_die = die_1 + die_2 
    total_die = str(total_die)
    person_error = 1
    # welcome and initial input - computer chooses number and asks you for your number 
    person_guess = input("Welcome to the game! To play the dice roll game, you and the computer will choose a number between 1 and 12, and two dice are rolled. Whoever has the number equal to the sum of the values on the two dice wins. Enter a number to begin: ")
    while person_guess != str(person_error):
        person_error = person_error + 1
        if person_error == 13:
            person_error = 1 
            person_guess = input("Please choose an integer between 1 and 12: ")
    # assign results variables (second one is dependent on person_guess's value)
    results_part_1 = str(die_1) + " (First die) + " + str(die_2) + " (Second die) = " + str(total_die)
    results_part_2 = "\nYour number was: " + str(person_guess) + "\nComputer's number was: " + str(computer_guess)
    # whoever's number is the same wins 
    if person_guess == total_die == computer_guess: 
        play_again = input(str(results_part_1) + str(results_part_2) + "\nYou both win! How rare. Play again? y/n: ").lower()
        return play_again
    elif person_guess == total_die:
        play_again = input(str(results_part_1) + str(results_part_2) + "\nYou win! Play again? y/n: ").lower()
        return play_again 
    elif computer_guess == total_die:
        play_again = input(str(results_part_1) + str(results_part_2) + "\nYou lost. :( Play again? y/n: ").lower()
        return play_again
    else:
        play_again = input(str(results_part_1) + str(results_part_2) + "\nLooks like no one won this round. Play again? y/n: ").lower()
        return play_again
# play the game and assign play_again to decide if the player wants to play again 
play_again = main()
# run code and the loop
while True:
    if play_again == "n":
        break
    elif play_again == "y":
        play_again = main()
    else:
        play_again = input("Please input y for yes or n for no: ").lower()
print("Come play again soon!")