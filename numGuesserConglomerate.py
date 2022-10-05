maximum = 100
minimum = 0
compguess = False
randomMode = True
if randomMode:
    from random import randint as r
hlc = ""
guess = ""
guess2 = maximum + 1
number = r(minimum, maximum)
if not compguess:
    input("I will choose a number from " + str(minimum) + " to " + str(maximum) + " and you will try to guess it.\nPress enter to continue\n")
else:
    input("To play this game, I will ask you if <insert number here> is your number.\nIf your number is higher than the guess, then input h.\nIf lower, input l.\nAnd if my guess is correct, input c.\n\nThink of a WHOLE NUMBER between " + str(minimum) + " and " + str(maximum) + " and then press enter.\n")
while True:
    if compguess:
        hlc = ""
        if randomMode:
            try: guess = r(minimum, maximum)
            except ValueError: print("Either me or you messed up. Probably you."); break
        else: guess = round((minimum + maximum) / 2)
        if guess2 == guess: print("Either me or you messed up. Probably me."); break
        guess2 = guess
        while hlc != "h" and hlc != "l" and hlc != "c": hlc = input("Is your number " + str(guess) + "?\n").lower()
        if hlc == "h": minimum = guess + 1
        elif hlc == "l": maximum = guess - 1
        elif hlc == "c": print("Haha!! I guessed your number! It was " + str(guess) + "!!!"); break
    else:
        guess = ""
        while guess == "":
            try:
              guess = int(input("Input a number between " + str(minimum) + " and " + str(maximum) + ": "))
              if guess > maximum or guess < minimum: guess = ""
            except: guess = ""
        if number > guess: print("Higher!"); minimum = guess + 1
        elif number < guess: print("Lower!"); maximum = guess - 1
        elif number == guess: print("You win! My number was " + str(guess)); break
