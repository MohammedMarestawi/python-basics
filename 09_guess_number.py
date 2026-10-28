def NUMBER_TO_GUESS():
    return 121

guess = 0
count = 0

while guess != NUMBER_TO_GUESS():
    guess = int(input("Give a positive integer: "))
    count += 1

    if guess > NUMBER_TO_GUESS():
        print("Your guess was too big")
    elif guess < NUMBER_TO_GUESS():
        print("Your guess was too small")

print(f"You guessed the value by {count} guesses! Nice!")