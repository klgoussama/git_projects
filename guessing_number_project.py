# random pour generer les nombre aleatoires et math pour les fonction math
import random
import math

# Taking Inputs pour la plage dans laquelle le nombre aléatoire sera généré. 
# Les entrées sont converties en entiers à l'aide de int()
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
 
# generating random number between [lower, upper] en utilisant randit du module random
x = random.randint(lower, upper)

# The formula round(math.log(upper - lower + 1, 2)) to calculate the minimum number of guesses required based on the range
print("\n\tYou've only ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0

# The loop will continue until the player guesses the correct number 
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses, shows this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")