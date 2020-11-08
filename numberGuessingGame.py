import random
number = random.randint(1, 10)
guess = int(input("Enter a number from 1 to 10: "))
while number != "guess":
    print
    if guess < number:
        print( "your guess is too low")
        guess = int(input("Enter a number from 1 to 10: "))
    elif guess > number:
        print("your guess is too high")
        guess = int(input("Enter a number from 1 to 10: "))
    else:
        print("you guessed it!")
        break
    print