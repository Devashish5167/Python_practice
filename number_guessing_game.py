import  random

def number_guessing_game():
    secret_number = random.randint(1,100)
    guess = None

    print("Welcome to the number guessing game! ")
    print("I,m thinking of a number between 1 and 100")
    print("Can you guess wht it is?")

    while guess != secret_number:
        guess = int(input("Enter your number: "))

        if guess<secret_number:
            print("Too low! try again ")
        elif guess>secret_number:
            print("Too high! try again ")
        else:
            print("Congratulations! you guessed the correct Number")

number_guessing_game()