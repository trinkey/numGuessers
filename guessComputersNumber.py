from random import randint as r
minimum = 0
maximum = 100
number = r(minimum, maximum)
guess = ""
input("I will choose a number from " + str(minimum) + " to " + str(maximum) + " and you will try to guess it.\nPress enter to continue\n")
while guess != number:
    guess = ""
    while guess == "":
        try:
          guess = int(input("Input a number between " + str(minimum) + " and " + str(maximum) + ": "))
          if guess > maximum or guess < minimum: guess = ""
        except: guess = ""
    if number > guess: print("Higher!"); minimum = guess + 1
    elif number < guess: print("Lower!"); maximum = guess - 1
    elif number == guess: print("You win! My number was " + str(guess))
