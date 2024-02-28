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
        guess = input(f"Sorry, try again! Or enter q to quit. You have {i} attempts remaining. ")
        if i == 1:
            print(f"You are out of attempts! The number was {number}")
        
