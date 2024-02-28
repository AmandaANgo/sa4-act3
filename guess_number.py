number = 10
i = 5

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q' and i > 1:
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        i -= 1
        if int(guess) > number:
            guess = input(f"Sorry, your guess is too high. Try again or enter q to quit. You have {i} attempt(s) remaining. ")
        else:
            guess = input(f"Sorry, your guess is too low. Try again or enter q to quit. You have {i} attempt(s) remaining. ")
        if i == 1:
            print(f"You are out of attempts! The number was {number}")
        


