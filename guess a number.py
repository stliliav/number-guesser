import random
global list_of_numbers
list_of_numbers = [str(i) for i in range(0,1000)]

def syntaxis(guess): 
    while not(guess in list_of_numbers):
        guess = input("This value should be an integer in range from 1 to 999! Try again\n")
        if guess in list_of_numbers:
            return int(guess)
            break

main_menu = print("Hello! Try to guess the number that I selected. Press 0 to leave the game")
number = random.choice(list_of_numbers)
global guess
guess = input()
syntaxis(guess)
while main_menu!=0 or guess!=number:
    if guess == number:
        won = print("You are absolutely right! Game is over")
        break
    if guess < number:
        guess = input("The number should be bigger. Try again!\n")
        syntaxis(guess)
    if guess > number:
        guess = input("The number should be smaller. Try again!\n")
                

    
    
