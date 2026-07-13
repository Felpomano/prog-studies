import random

print("Welcome to the guessing game!")

play_again = True

while play_again:
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:  
        tryy = int(input("Input a number between 1 and 100: "))   
        attempts += 1

        if tryy < secret_number:
            print("Too low! Try again.")
        elif tryy > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You got the right number in {attempts} attempts.")
            break

    answer = input("Do you want to play again? (y/n): ").strip().lower()
    if answer != "y":
        play_again = False
        print("Thanks for playing!")            

