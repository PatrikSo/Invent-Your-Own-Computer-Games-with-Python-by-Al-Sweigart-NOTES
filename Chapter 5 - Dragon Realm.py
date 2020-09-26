'''Tpics to be covered:
Topics to be covered:
Flowcharts
Creating your own functions with the def keyword
Multiline strings
while statements
The and, or, and not Boolean operators
Truth tables
The return keyword
Global and local variable scope
Parameters and arguments
The sleep() function

making the,
DRAGON REALM game:
player is in a land full of dragons, they all live in caves.
Some will share their treasure, some will eat you.
Player chooses between two caves, one is bad and one is good!
'''

import random       #random library
import time         #Time library

def displayIntro():             #function to display intro text
    print(" Your are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure. The other dragon is greedy and will eat you on sight!")
    print()

def chooseCave():               #function that lets you choose a cave
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):      #function that responds to your choice
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
                                #part of functions that lets you replay 
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()



'''
Can create flowcharts to help design games (pic not included)
    branches of the player path
def statements let you define functions for reusable code.
calling a function means you are using that code segment.
time Modules let you time events, such as delayed print statements.
while loops run until its given condition is false (boolean statement).
Multi-line strings just use \n in the line for more lines.
Boolean statements can have several conditions (one large multi-condition)
    Using 'and' and 'or' statements, and, or
'''

'''Chapter summary:
Function is a mini-program within your program.
Variable scopes are their lifespan's. Where you can/cannot use a variable.
A variable with a global scope can be used anywhere in the program.
Local scope variables can only be used in a certain area.
