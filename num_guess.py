integer = int(input("Enter the integer for the player to guess.\n"))
print("Enter your guess.")
guess = int(input())
tracker = 1
while guess != integer:
    tracker = tracker + 1
    if guess < integer:
        guess = int(input("Too low - try again:\n"))
    elif guess > integer:
        guess = int(input("Too high - try again:\n"))
if tracker == 1:
    print("You guessed it in", tracker, "try.")
elif tracker > 1:
    print("You guessed it in", tracker, "tries.")