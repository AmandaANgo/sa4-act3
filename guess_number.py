number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input("Sorry, try again! Or enter q to quit. ")

