'''Topics to be covered:
import statements
Modules
The randint() function
for statements
Blocks
The str(), int(), and float() functions
Booleans
Comparison Operators
Conditions
The difference between = and ==
if statements
break statements

making the,
Guess The Number Game:
Game makes you guess a number between 1 to 20.
It will let you know if your guess is too high or too low.
You only have 6 tries!
'''

# This is a Guess the Number game.
import random

guessesTaken = 0;

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for i in range(6):              #for loop to give player 6 guesses
    print('Take a guess.')      #Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    guessesTaken += 1           #Increments guessesTaken

    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break                           # break sequence immediatly 

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job, ' + myName + '! You guessed my number in ' + guessesTaken
          + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')



''' Chapter 3 summary
Expressions: values connected by operators
Assignment statements: store values in variables for later use
The if,for, and break statemenrs: control flow statements
    let you skip execution of certain lines of code
The print() and input() functions: prints to screen and gets input
'''
