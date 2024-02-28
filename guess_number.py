number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        if int(guess) > number:
            guess = input("Sorry, your guess is too high. Try again or enter q to quit. ")
        else:
            guess = input("Sorry, your guess is too low. Try again or enter q to quit. ")

