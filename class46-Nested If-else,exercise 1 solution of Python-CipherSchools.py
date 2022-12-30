'''Exercise, number guessing game
make a variable, like winning_number and assign any number to it.
ask user to guess a number.
if user guessed correctly then print "You Win !!!"
if user didn't guessed correctly then:
    if user guessed lower than actual number then print "too low"
    if user guessed higher than actual number then print "too high"

google "how to generate random number in python " to generate random
winning number'''


winning_number = 27
user_input = int(input("guess a number b/w 1 and 100 : "))
if user_input == winning_number:
    print("You Win !!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")
