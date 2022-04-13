integer = int(input("Enter the integer for the player to guess.\n"))
print("Enter your guess.")
guess = int(input())
tracker = 1
while guess != integer:
    tracker = tracker + 1
    if guess < integer:
        print ("Too low - guess again:")
        guess = int(input())
    elif guess > integer:
        print ("Too high - guess again:")
        guess = int(input())
if tracker == 1:
    print("You guessed it in ", tracker, " try.")
elif tracker > 1:
    print("You guessed it in ", tracker, " tries.")