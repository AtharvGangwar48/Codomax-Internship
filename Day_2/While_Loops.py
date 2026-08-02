secret_number = 7
user_guess = 0

print("Welcome! Can you guess my secret number between 1 and 10?")

# The loop keeps repeating as long as the guess is incorrect
while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Spot on! You guessed the secret number.")
