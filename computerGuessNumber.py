maximum = 100
minimum = 0
hlc = ""
guess2 = maximum + 1
input("To play this game, I will ask you if <insert number here> is your number.\nIf your number is higher than the guess, then input h.\nIf lower, input l.\nAnd if my guess is correct, input c.\n\nThink of a WHOLE NUMBER between " + str(minimum) + " and " + str(maximum) + " and then press enter.\n")
while hlc != "c":
    hlc = ""
    guess = round((minimum + maximum) / 2)
    if guess2 == guess: print("Either me or you messed up. Probably me."); break
    guess2 = guess
    while hlc != "h" and hlc != "l" and hlc != "c": hlc = input("Is your number " + str(guess) + "?\n").lower()
    if hlc == "h": minimum = guess + 1
    elif hlc == "l": maximum = guess - 1
    elif hlc == "c": print("Haha!! I guessed your number! It was " + str(guess) + "!!!")
